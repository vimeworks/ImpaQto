from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^coworkers/lista/$',views.coworker,name='coworker.listado'),
    url(r'^coworkers/registro/$',views.registro_coworker_view,name='coworker.registro'),
    url(r'^membresias/lista/$',views.list_membresia_view,name='membresia.listado'),
    url(r'^membresias/registro/$',views.registro_membresia_view,name='membresia.registro'),
    url(r'^contrato/lista/$',views.list_contratos_view,name='contrato.listado'),
    url(r'^contrato/registro/$',views.registro_contrato_membresia_view,name='contrato.registro'),
]