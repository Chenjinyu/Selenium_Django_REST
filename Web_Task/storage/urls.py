from django.conf.urls import url
from storage import views

urlpatterns = [
    url(r'^storage/$', views.storage_list),
    url(r'^storage/(?P<pk>[0-9]+)/$', views.storage_detail),
]