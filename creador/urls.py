from django.conf.urls import url
from creador import views
#from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^login/$', views.login),
	#url(r'^usuario/$', views.addUsuario),
]
