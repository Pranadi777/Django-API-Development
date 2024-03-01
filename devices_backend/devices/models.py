import uuid
from django.db import models
from django_extensions.db.fields import AutoSlugField

# Create your models here.

#every device in the application has a location
class Location(models.Model):
    #can give lat/long meta data in the first, sticking with just location name for now
    #e.g., office, greenhous
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    name = models.CharField(max_length=200)
    #want a slug for each device
    #e.g., CO2 Sensor -> co2-sensor
    slug = AutoSlugField(populate_from='name')
    location = models.ForeignKey(
        Location,
        #if location is deleted, set value to device to Null
        on_delete=models.SET_NULL,
        null=True,
        #when adding a new device on form, no need to specific location with blank=True
        blank=True
    )

    def __str__(self):
        return f"{self.name} - {self.id}"