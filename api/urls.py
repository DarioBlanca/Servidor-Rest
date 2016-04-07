from django.conf.urls import url
from api import views
#from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^conexion/$', views.conexion),
	url(r'^desconexion/$', views.desconexion),
]