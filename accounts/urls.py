from django.conf.urls import url
from . import views

urlpatterns = [
               url(r'^$',views.index_view,name='accounts.index'),
               url(r'^login/$',views.login_view,name='accounts.login'),
               url(r'^logout/$',views.logout_view,name='accounts.logout'),
               url(r'^userprofile/registro/$',views.registro_usuario_view,name='accounts.registro.userprofile'),
               url(r'^userprofile/lista/$',views.list_usuarios_view,name='accounts.listado.userprofile'),
               url(r'^userprofile/edicion/(?P<pk>\d+)/$',views.editar_accounts,name='accounts.edicion.userprofile'),
               ]