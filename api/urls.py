from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^',include('coworkersimpaqto.urls')),
    url(r'^hola_mundo_rest/(?P<username>\w+)/$',views.hola_mundo),
    url(r'^coworker/$',views.coworker),
    url(r'^coworker/(?P<username>\w+)/$',views.coworker),
    url(r'^contrato/$',views.contrato),
    url(r'^contrato/(?P<username>\w+)/$',views.contrato),
    url(r'^consumo/(?P<username>\w+)/$',views.consumo),
]