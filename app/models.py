from django.db import models
from site_.settings import MEDIA_ROOT

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


class Avaliacao(models.Model):
	candidato = models.ForeignKey(Candidato)
	criterio = models.ManyToManyField(Criterio, default = '')
	value = models.IntegerField(default = 0, db_index = True)
	avaliador = models.ForeignKey('auth.User')

	def  __str__(self):
		return self