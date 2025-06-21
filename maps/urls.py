from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view),
    path('states/', views.get_states),
    path('districts/<int:state_id>/', views.get_districts),
    path('talukas/<int:district_id>/', views.get_talukas),
    path('villages/<int:taluka_id>/', views.get_villages),
    path('village-data/<int:id>/', views.village_data),

    # ✅ GeoJSON endpoints for polygon highlighting
    path('state-geojson/<int:state_id>/', views.state_geojson),
    path('district-geojson/<int:district_id>/', views.district_geojson),
    path('taluka-geojson/<int:taluka_id>/', views.taluka_geojson),
    path('village-geojson/<int:village_id>/', views.village_geojson),
]
