from django.contrib import admin
from .models import Criterio, Candidato, Avaliacao

admin.site.register(Candidato)
admin.site.register(Criterio)
admin.site.register(Avaliacao)