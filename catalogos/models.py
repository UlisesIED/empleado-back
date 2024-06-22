from django.db import models

class Puesto(models.Model):
    descripcion = models.CharField(unique= True, null=False, max_length=128)
    
class Parentesco(models.Model):
    descripcion = models.CharField(unique= True, null=False, max_length=128)

