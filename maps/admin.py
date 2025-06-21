from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import State, District, Taluka, Village

@admin.register(State)
class StateAdmin(LeafletGeoAdmin):
    list_display = ('name',)

@admin.register(District)
class DistrictAdmin(LeafletGeoAdmin):
    list_display = ('name',)

@admin.register(Taluka)
class TalukaAdmin(LeafletGeoAdmin):
    list_display = ('name',)

@admin.register(Village)
class VillageAdmin(LeafletGeoAdmin):
    list_display = ('name',)
