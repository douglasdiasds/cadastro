from .models import Candidato, Criterio
from django import forms

class CandForm(forms.ModelForm):
	class Meta:
		model = Candidato
		fields = ('name', 'e_mail', 'github', 'linkedin', 'Ensino_superior','cover_letter')

class AvalForm(forms.ModelForm):
	class Meta:
		model = Criterio
		fields = ('label',)
