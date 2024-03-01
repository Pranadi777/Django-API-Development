from ninja import ModelSchema
from devices.models import Device, Location

#Schemas are used to determine th structure of the data  coming in to the 
#api end poitns, and the data returned from the data endpoints

#inherets from ninja's ModelSchema class
class LocationSchema(ModelSchema):
    class Meta:
        model = Location
        fields = ('id', 'name')


class DeviceSchema(ModelSchema):
    #location will be nested since it's coming from another schema
    #if the location schema is not matched (meaning null), set to none
    location: LocationSchema | None = None

    class Meta:
        model = Device
        fields = ('id','name','slug','location')