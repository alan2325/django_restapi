from django.db import models

# Create your models here.
class std(models.Model):
    name=models.TextField()
    age=models.IntegerField()
    mark=models.IntegerField()
    