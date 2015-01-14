from django.db import models

class image(models.Model):
    id_image = models.IntegerField()
    created = models.DateField()
    size = models.IntegerField()
    virtual_size = models.IntegerField()

class repository(models.Model):
	url = models.CharField(max_length=200)
	description = models.CharField(max_length=100)
    
    