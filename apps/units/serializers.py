from apps.units import models
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers

# REST framework serializer
# http://www.django-rest-framework.org/tutorial/quickstart


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Unit
        # json id field is called pk in Django-rest-framework
        fields = ('id', 'name', 'status', 'desc')


class CountiesSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.County
        geo_field = 'geom'
        fields = ('id', 'name')
