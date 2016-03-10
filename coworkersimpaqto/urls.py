from django.conf.urls import url, include
from . import views

#from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'rest/membresia',views.ContratoViewSet)
##router.register(r'rest/contrato/(?P<id>[0-9]+)/$',views.ContratoDetailViewSet)
#router.register(r'rest/coworker',views.CoworkerViewSet,"coworker")




urlpatterns = [
    url(r'^$',views.index,name='index'),
    #url(r'^',include(router.urls)),
    url(r'^coworkers/lista/$',views.coworker,name='coworker.listado'),
    url(r'^coworkers/registro/$',views.registro_coworker_view,name='coworker.registro'),
    url(r'^coworkers/edicion/(?P<pk>\d+)/$',views.editar_dos_coworker,name='coworker.edicion'),
    #url(r'^coworkers/edicion/(?P<pk>\d+)/$',views.CoworkerUpdate.as_view(),name='coworker.edicion'),
    url(r'^membresias/lista/$',views.list_membresia_view,name='membresia.listado'),
    url(r'^membresias/registro/$',views.registro_membresia_view,name='membresia.registro'),
    url(r'^membresias/edicion/(?P<pk>\d+)/$',views.editar_membresia,name='membresia.edicion'),
    url(r'^contrato/lista/$',views.list_contratos_view,name='contrato.listado'),
    url(r'^contrato/registro/$',views.registro_contrato_membresia_view,name='contrato.registro'),
    url(r'^contrato/edicion/(?P<pk>\d+)/$',views.editar_contrato,name='contrato.edicion'),
    url(r'^jsonp/$',views.reportes,name='jsonp')
    #url(r'^rest/contrato/(?P<id>[0-9]+)/$',views.ContratoDetailViewSet)
    ##url(r'^contrato/rest/(?P<codigo>[0-9]+)/$',views.contrato_detail_view,name='contrato.rest.identificar'),
]