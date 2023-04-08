from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
