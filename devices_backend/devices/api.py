from ninja import NinjaAPI
from devices.models import Device, Location
from devices.schemas import DeviceSchema, LocationSchema, DeviceCreateSchema, Error, DeviceLocationPatch
from django.shortcuts import get_object_or_404

#Django ninja API endpoints in this file -  hooked to URLs. think of this like views.py file

#Notes:
#response will be the json data (converted from the query set Device.objects.all()) by the DeviceSchema structure. i.e., DjangoNinja ModelSchema converts querysets into jsonn
#So schema provides validation of structure of the data and documentation of the endpoint
#endpoints arecreated with decorators


#Instantiate Ninja API object
app = NinjaAPI()

#Endpoint that returns all devices
@app.get("devices/", response=list[DeviceSchema])
def get_devices(request):
    return Device.objects.all()

#Endpoint that return one specific device.
@app.get("devices/{slug}/", response = DeviceSchema)
def get_device(request, slug: str):
    device = get_object_or_404(Device, slug= slug)
    return device

#endpoint that returns all locations
@app.get("locations/", response=list[LocationSchema])
def get_locations(request):
    return Location.objects.all()

#post request to devices endpoint to create new device
#response is DeviceSchema since we are returning the created obejct. If 404, response to client will be Error Schema
@app.post("devices/", response={200:DeviceSchema, 404: Error})
#to create, you need a schema for the request body -> DeviceCreateSchema
#then, declare this schema as a parameter to the api handler function (below)
def create_device(request, device: DeviceCreateSchema):
    #perform lookup to see if location has been passes
    if device.location_id:
        location_exists = Location.objects.filter(id= device.location_id).exists()
        if not location_exists:
            return 404, {'message': 'Location not found'}


    #information given by the post request will be in 'device' as an instance of the DeviceCreateSchema class. So convert it to a dictionary by using model_dump(). 
    device_data = device.model_dump()
    #then create a new row in the data base using the keys and values from the now dictionary
    device_model = Device.objects.create(**device_data)
    return device_model

#location here is the request body
@app.post('devices/{device_slug}/set-location/', response=DeviceSchema)
def update_device_location(request, device_slug, location: DeviceLocationPatch):
    device = get_object_or_404(Device, slug=device_slug)
    if location.location_id:
        location = get_object_or_404(Location, id=location.location_id)
        device.location = location
    else:
        device.location = None
    device.save()

    #again return instance of device model, ninja will expect it in the response (which it will convert using the DeviceSchema)
    return device