from django.contrib.gis.db import models
from django.contrib.gis.geos import MultiPolygon  # ✅ Required for default geometry

class State(models.Model):
    name = models.CharField(max_length=100)
    geom = models.MultiPolygonField(null=True, blank=True)
  # ✅ Default empty polygon

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    geom = models.MultiPolygonField(null=True, blank=True)
  # ✅ Default empty polygon

    def __str__(self):
        return self.name

class Taluka(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    geom = models.MultiPolygonField(null=True, blank=True)
  # ✅ Default empty polygon

    def __str__(self):
        return self.name

class Village(models.Model):
    name = models.CharField(max_length=100)
    taluka = models.ForeignKey(Taluka, on_delete=models.CASCADE)
    geom = models.MultiPolygonField(null=True, blank=True)
  # ✅ Default empty polygon
    population = models.IntegerField(default=0)
    info = models.TextField(default="")

    def __str__(self):
        return self.name

class VillageData(models.Model):
    village = models.OneToOneField('Village', on_delete=models.CASCADE)
    population = models.IntegerField(default=0)
    info = models.TextField(default="")
    data_point = models.PointField(null=True, blank=True)

    def __str__(self):
        return f"{self.village.name} - {self.data_point}"
