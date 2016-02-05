from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^coworkers/lista/$',views.coworker,name='coworker.listado'),
    url(r'^coworkers/registro/$',views.registro_coworker_view,name='coworker.registro'),
]