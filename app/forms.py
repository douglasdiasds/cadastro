from .models import Candidate, Evaluation
from django import forms

class CandForm(forms.ModelForm):
	class Meta:
		model = Candidate
		fields = ('name', 'e_mail', 'github', 'linkedin', 'higher_education','cover_letter')

class EvalForm(forms.ModelForm):
	class Meta:
		model = Evaluation
		fields = ('candidate','criterion','score','appraiser')
		#fields = ('v1','v2')
		