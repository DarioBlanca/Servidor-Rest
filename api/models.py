from django.db import models
from django.contrib.auth.models import User 

class RegistroIPs(models.Model):
	ippublica = models.TextField(max_length=16)
	ipprivada = models.TextField(max_length=16)

class TablaIntermedia(models.Model):
	ips = models.ForeignKey('RegistroIPs')
	usuario = models.ForeignKey(User)
	estado = models.BooleanField(default=True)