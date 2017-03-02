#from .models import Candidato
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.canditato_list, name='canditato_list'),
	#url(r'^avaliacao/$', views.avaliacao, name='avaliacao')
	url(r'^candidato/(?P<pk>[0-9]+)/$', views.candidato_detalhe, name='candidato_detalhe'),
	#url(r'^candidato/new/$', views.cadastrar, name='cadastrar'), 	<-- o botao fica na msm page que lista cand
	url(r'^candidato/[0-9]+/new/$', views.cadastrar, name='cadastrar'),				# <-- o botao fica num link independete
	#url(r'^avaliacao/$', views.avaliar, name='avaliar'), 

]