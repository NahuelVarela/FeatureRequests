from django.db import models

# Create your models here.

class FeaturesItems(models.Model):
	owner = models.CharField(max_length=60)
	handler = models.CharField(max_length=60, default="Sin Asignar")
	status = models.CharField(max_length=60, default="Proposed")
	title = models.CharField(max_length=60, blank=False)
	description = models.TextField()
	last_modify_date = models.DateField(auto_now=True)
	created_date = models.DateField(auto_now_add=True)