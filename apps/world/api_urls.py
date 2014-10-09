from django.conf.urls import patterns, include, url
from apps.world import json_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url('^world$', json_views.WorldCollection.as_view(), name='world'),
)
