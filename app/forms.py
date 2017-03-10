from .models import Candidato, Avaliacao
from django import forms

class CandForm(forms.ModelForm):
	class Meta:
		model = Candidato
		fields = ('name', 'e_mail', 'github', 'linkedin', 'Ensino_superior','cover_letter')

class AvalForm(forms.ModelForm):
	class Meta:
		model = Avaliacao
		fields = ('criterio','avaliador','value','candidato')
