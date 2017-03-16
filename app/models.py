from django.db import models
from jsonfield import JSONField
from site_.settings import MEDIA_ROOT
from django.core.validators import MaxValueValidator

class Criterio(models.Model):
	label = models.CharField(max_length=100)

	def  __str__(self):
		return self.label

class Candidato(models.Model):
	name = models.CharField(max_length=100)
	e_mail = models.EmailField(max_length=100, default = '')
	github = models.URLField(default = '')
	linkedin = models.URLField(max_length=100, default = '')
	cover_letter = models.TextField(default = '')
	Ensino_superior = models.BooleanField(default = False)
	med = models.IntegerField(default = 0)
	#talvez tenha que alterrar essa linha
	docfile = models.FileField(upload_to='/home/douglas/Documentos/Django/my-second-blog/site_/media', null=True, blank=True)

	def  __str__(self):
		return self.name

class Aval(models.Model):
	criterio = models.ManyToManyField(Criterio)
	nota = models.IntegerField()

	def  __str__(self):
		return self


class Avaliacao(models.Model):
	candidato = models.ForeignKey(Candidato)
	criterio = models.ForeignKey(Criterio, default='')
	nota = models.PositiveIntegerField(default = 0, validators=[MaxValueValidator(10)])
	avaliador = models.ForeignKey('auth.User')

	def  __str__(self):
		return self