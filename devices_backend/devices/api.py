#Django ninja API in this file -  hooked to URLs

from ninja import NinjaAPI
from devices.models import Device, Location
from devices.schemas import DeviceSchema, LocationSchema
from django.shortcuts import get_object_or_404

#Instantiate Ninja API object
app = NinjaAPI()

#endpoint that allows to fetch all devices in the database
#response will be the json data (converted from the query set Device.objects.all()) by the DeviceSchema structure
#So schema provides validation of structure of the data and documentation of the endpoint
#endpoints created with decorators
#Think of this like a views.py (see urls.py file)
@app.get("devices/", response=list[DeviceSchema])
def get_devices(request):
    return Device.objects.all()

#return one specific device.
#can remove the list[] since it's just one object
#Again, the ninja ModelSchema, knows how to convert the model instance into json
@app.get("devices/{slug}/", response = DeviceSchema)
def get_device(request, slug: str):
    device = get_object_or_404(Device, slug= slug)
    return device


@app.get("locations/", response=list[LocationSchema])
def get_locations(request):
    return Location.objects.all()