from django.conf.urls import patterns, include, url
from django.contrib import admin


api_patterns = patterns('',
    url(r'^', include('apps.units.api_urls'), name='units'),
    url(r'^', include('apps.units.api_urls'), name='counties'),
    url(r'^', include('apps.world.api_urls'), name='world'),
)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.units.urls', namespace='units')),
    url(r'api/v1/', include(api_patterns, namespace='api')),
)