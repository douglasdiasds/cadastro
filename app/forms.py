from .models import Candidate, Evaluation, Teste
from django import forms

class CandForm(forms.ModelForm):
	class Meta:
		model = Candidate
		fields = ('name', 'e_mail', 'github', 'linkedin', 'higher_education','cover_letter')

class EvalForm(forms.ModelForm):
	class Meta:
		model = Evaluation
		fields = ('candidate','criterion','score','appraiser')


#formulário de teste
class TestForm(forms.ModelForm):
	class Meta:
		model =  Teste
		fields = ('nome',)
			
		
		