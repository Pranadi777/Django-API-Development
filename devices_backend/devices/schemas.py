from ninja import ModelSchema, Schema
from devices.models import Device, Location

# - Schemas are used to determine th structure of the data  coming in to the api end poitns, and the data returned from the data endpoints
# - When requesting data: Schemas inheret from ninja's ModelSchema class (since data is coming from a model)
# - When posting data: Schema inherets from ninjas's Schema, using a request body


#Schema for returning location data
class LocationSchema(ModelSchema):
    class Meta:
        model = Location
        fields = ('id', 'name')

#Schema for returning device data
class DeviceSchema(ModelSchema):
    #location will be nested since it's coming from another schema
    #if the location schema is not matched (meaning null), set to none
    location: LocationSchema | None = None

    class Meta:
        model = Device
        fields = ('id','name','slug','location')

#Schema to add a device
#no need to give it an id since that is generate automatically. Niether the slug
class DeviceCreateSchema(Schema):
    name: str
    location_id: int | None = None

#Schema for error
class Error(Schema):
    message: str

#Schema for an API endpoint that allows a client to change the location
class DeviceLocationPatch(Schema):
    location_id: int | None = None