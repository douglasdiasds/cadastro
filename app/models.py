from django.db import models
from jsonfield import JSONField
from site_.settings import MEDIA_ROOT
from django.core.validators import MaxValueValidator

class Criterion(models.Model):
	label = models.CharField(max_length=100)

	def  __str__(self):
		return self.label

class Candidate(models.Model):
	name = models.CharField(max_length=100)
	e_mail = models.EmailField(max_length=100, default = '')
	github = models.URLField(default = '')
	linkedin = models.URLField(max_length=100, default = '')
	cover_letter = models.TextField(default = '')
	higher_education = models.BooleanField(default = False)
	average = models.IntegerField(default = 0)
	#############################################################score = models.ForeignKey()
	docfile = models.FileField(upload_to='/home/douglas/Documentos/Django/my-second-blog/site_/media', null=True, blank=True)

	def  __str__(self):
		return self.name


class Evaluation(models.Model):
	candidate = models.ForeignKey(Candidate, unique=True)
	criterion = models.ForeignKey(Criterion, default='')
	score = models.PositiveIntegerField(default = 0, validators=[MaxValueValidator(10)])
	appraiser = models.ForeignKey('auth.User')

	def  __str__(self):
		return str(self.candidate)


class avarage(models.Model):
	eva = Evaluation.objects.get()



