from django.conf.urls import url, include
from django.contrib import admin
from . import views

from django.views.generic import ListView
from HP_SimplifiedConfig.models import ProLiant_DL_Server, ProLiant_DL300_Servers, ProLian_DL_Customize_Factory,\
Memory_DB, Storage_DB, Processor_DB

urlpatterns = [
    url(r'^$', views.new_conf, name = 'new_conf'),
#     url(r'^(?P<num>[0-9]+)/$', views.proliant_dl_server, name = 'proliant_dl_server'),
    url(r'^(?P<num>[0-9]+)/$', ListView.as_view(queryset = ProLiant_DL_Server.objects.all().order_by('id'), 
template_name="proliant_dl_server.html")),
    url(r'^(?P<num>[0-9]+)/([0-9]{2})/$', ListView.as_view(queryset = ProLiant_DL300_Servers.objects.all().order_by('id'), 
template_name="proliant_dl300_server.html")),
    url(r'^(?P<num>[0-9]+)/([0-9]{2})/([0-9]{3})/$', ListView.as_view(queryset = ProLian_DL_Customize_Factory.objects.all().order_by('id'), 
template_name="proliant_dl_customize.html")),
    url(r'^(?P<num>[0-9]+)/([0-9]{2})/([0-9]{3})/([0-9]{4})/$', ListView.as_view(queryset = ProLian_DL_Customize_Factory.objects.all().order_by('id'), 
template_name="config_page.html")),
    url(r'^request/memory/$', ListView.as_view(queryset = Memory_DB.objects.all().order_by('id'), 
template_name="memory_info.html")),
    url(r'^request/processor/$', ListView.as_view(queryset = Processor_DB.objects.all().order_by('id'), 
template_name="processor_info.html")),
    url(r'^request/storage/$', ListView.as_view(queryset = Storage_DB.objects.all().order_by('id'), 
template_name="storage_info.html")),
]
