from django.db import models

# Create your models here.
class std(models.Model):
    name=models.TextField()
    age=models.IntegerField()
    roll=models.IntegerField()
    
    def __str__(self):
        return self.name