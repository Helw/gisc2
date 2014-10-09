from apps.world import models
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers

# REST framework serializer
# http://www.django-rest-framework.org/tutorial/quickstart


class WorldSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.WorldBorder
        geo_field = 'mpoly'
        fields = ('name', 'area', 'pop2005', 'fips', 'iso2', 'iso3', 'un', 'region', 'subregion', 'lon', 'lat', 'mpoly')

