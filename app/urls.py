#from .models import Candidato
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.canditato_list, name='canditato_list'),
	url(r'^candidato/(?P<pk>[0-9]+)/$', views.candidato_detalhe, name='candidato_detalhe'),
]