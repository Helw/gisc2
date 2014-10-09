from django.conf.urls import patterns, include, url
from apps.units import views
from django.contrib import admin


urlpatterns = patterns('',


    url(r'^admin/', include(admin.site.urls)),
    url(r'^main$', views.MainView.as_view()),
    url(r'^about$', views.AboutView.as_view()),

)