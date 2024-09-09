from django.db import models

# Create your models here.
class DestinationData(models.Model):
    dest_name = models.CharField(max_length=50)
    dest_desc = models.CharField(max_length=10000)