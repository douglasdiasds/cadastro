from .models import Candidato, Avaliacao#, Aval
from django import forms

class CandForm(forms.ModelForm):
	class Meta:
		model = Candidato
		fields = ('name', 'e_mail', 'github', 'linkedin', 'Ensino_superior','cover_letter')

class AvalForm(forms.ModelForm):
	class Meta:
		model = Avaliacao
		fields = ('criterio','nota','candidato','avaliador')
		"""
		model = Avaliacao
		fields = ('candidato','avaliador','aval',)
		"""
