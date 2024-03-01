from django.contrib import admin
from django.urls import path
from devices.api import app

urlpatterns = [
    path('admin/', admin.site.urls),
    #reference urls from the app object in the api file (endpoints with decorators)
    path('api/', app.urls)
]
