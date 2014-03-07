from django.db import models

from attendees.models import Attendee

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    Presenter = models.ManyToManyField(Attendee, blank=True)
    date = models.DateField()
    starttime = models.TimeField()
    endtime = models.TimeField()
    room = models.CharField(max_length = 200)
    track = models.CharField(max_length = 200, blank=True)
    level = models.CharField(max_length = 200, blank=True)
    details = models.TextField()
    def __str__(self):
        return self.title
    