from django.db import models

# Create your models here.
class task(models.Model):
    task=models.CharField(max_length=150)
    priority=models.CharField(max_length=100)
    time=models.TimeField(blank=True, default='', null=True)
    date=models.DateField()
    
    def __str__(self):
        return self.task