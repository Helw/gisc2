from apps.world import models, serializers
from rest_framework import generics
import django_filters

# views section of quick start guide
# http://www.django-rest-framework.org/tutorial/quickstart



class IntegerListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split(',')]
            return qs.filter(**{'{}__{}'.format(self.name, self.lookup_type): integers})
        return qs


class WorldFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.WorldBorder
        fields = ['name', 'area']


class WorldCollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.WorldBorder.objects.all()
    serializer_class = serializers.WorldSerializer
    filter_class = WorldFilter