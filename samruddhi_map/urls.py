from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('maps.urls')),  # make sure 'maps' is the app name
]
