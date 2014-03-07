from django.db import models

# Create your models here.

class Attendee(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, blank=True)
    organization = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=254)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return '{0} {1}'.format(self.firstname, self.lastname)
