from django.contrib import admin
from .models import Criterio, Candidato, Avaliacao, Teste

admin.site.register(Candidato)
admin.site.register(Criterio)
admin.site.register(Avaliacao)
#admin.site.register(Teste)