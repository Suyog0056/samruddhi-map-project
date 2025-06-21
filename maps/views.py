from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import State, District, Taluka, Village


def map_view(request):
    return render(request, 'maps/map.html')


def get_states(request):
    states = State.objects.all().values("id", "name")
    return JsonResponse(list(states), safe=False)

def get_districts(request, state_id):
    districts = District.objects.filter(state_id=state_id).values("id", "name")
    return JsonResponse(list(districts), safe=False)

def get_talukas(request, district_id):
    talukas = Taluka.objects.filter(district_id=district_id).values("id", "name")
    return JsonResponse(list(talukas), safe=False)

def get_villages(request, taluka_id):
    villages = Village.objects.filter(taluka_id=taluka_id).values("id", "name")
    return JsonResponse(list(villages), safe=False)

def village_data(request, id):
    village = get_object_or_404(Village, id=id)
    data = {
        "name": village.name,
        "population": village.population,
        "info": village.info,
    }
    return JsonResponse(data)


def state_geojson(request, state_id):
    geojson = serialize('geojson', State.objects.filter(id=state_id), geometry_field='geom', fields=('name',))
    return HttpResponse(geojson, content_type='application/json')

def district_geojson(request, district_id):
    geojson = serialize('geojson', District.objects.filter(id=district_id), geometry_field='geom', fields=('name',))
    return HttpResponse(geojson, content_type='application/json')

def taluka_geojson(request, taluka_id):
    geojson = serialize('geojson', Taluka.objects.filter(id=taluka_id), geometry_field='geom', fields=('name',))
    return HttpResponse(geojson, content_type='application/json')

def village_geojson(request, village_id):
    geojson = serialize('geojson', Village.objects.filter(id=village_id), geometry_field='geom', fields=('name',))
    return HttpResponse(geojson, content_type='application/json')
