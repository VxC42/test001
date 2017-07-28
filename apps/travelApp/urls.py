from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^travels$', views.travels, name='travels'),
    url(r'^join/(?P<id>\d+)$', views.join),
    url(r'^travels/add$', views.add, name='add'),
    url(r'^travels/destination/(?P<id>\d+)$', views.destination, name='destination'),
    url(r'^travels/addPlan$', views.addPlan, name='addPlan'),
    url(r'^logoff$', views.logoff, name='logoff'),
]
