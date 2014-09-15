from django.contrib.gis.db import models


class Unit(models.Model):
    """Add Docstring"""
    name = models.CharField(max_length=40)
    status = models.BooleanField()
    desc = models.CharField(max_length=280)

    def __str__(self):
        return "{}".format(self.name)


class County(models.Model):
    """Represents a US County."""
    name = models.CharField(max_length=60)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return "{}".format(self.name)