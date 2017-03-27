#from .models import Candidato
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.canditate_list, name='canditate_list'),
	url(r'^candidato/(?P<pk>[0-9]+)/$', views.candidate_detail, name='candidate_detail'),
	url(r'^cadastrar/$', views.register, name='register'),	# <--! o cadastro fica num link independete
	url(r'^grid/$', views.grid, name='grid'),
	url(r'^candidato/[0-9]+/avaliacao/$', views.evaluation, name='evaluate'), 

]