# Developing modern APIs with Django

![screenshot](api_docs.png)

## Description of Project:

- Gain an understanding of how API development works within a Django framework
- This API will allow userss to fetch and create IOT devices and also to assign devices to and from a location
- Build on the skill learned in this project to build an API for JobGenome

## Description of Django Ninja:

- Schemas (as defined in Schemas.py), instruct how data should be processed whether it is data input (POST) or data output (GET)
- app.py define the api endpoints/rouutes

## API Endpoints
The following endpoints are available:

GET api/devices/: Retrieve a list of all devices.
GET api/locations/: Retrieve a list of all locations.
GET api/devices/{slug}/: Retrieve a list of all locations.


POST /api/resource/: Create a new resource.
GET /api/resource/<id>/: Retrieve a specific resource.
PUT /api/resource/<id>/: Update a specific resource.
DELETE /api/resource/<id>/: Delete a specific resource


## Credit

following another amazing tutorial by Bugbytes:
https://www.youtube.com/watch?v=XqkqbsdtoMI&t=1555s