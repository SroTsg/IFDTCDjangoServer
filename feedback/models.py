from django.db import models
from django.forms import ModelForm

from agenda.models import Event

# Create your models here.

class ConferenceFeedback(models.Model):
    opinion = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=1000, blank=True)
    general = models.CharField(max_length=1000, blank=True)
    experience = models.CharField(max_length=1000, blank=True)
    more = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return 'Conference Feedback {0}'.format(self.id)

    

class SessionFeedback(models.Model):
    sessionID = models.ForeignKey(Event)
    expectations = models.CharField(max_length=1000, blank=True)
    knowledge = models.CharField(max_length=1000, blank=True)
    knowledgeable = models.CharField(max_length=1000, blank=True)
    understandable = models.CharField(max_length=1000, blank=True)
    rightAmount = models.CharField(max_length=1000, blank=True)
    recommend = models.CharField(max_length=1000, blank=True)
    comments = models.CharField(max_length=1000, blank=True)
    
    def __str__(self):
        return '{0} feedback'.format(self.sessionID)
    
class ConferenceForm(ModelForm):
    class Meta:
        model = ConferenceFeedback
        fields = ['opinion', 'location', 'general', 'experience', 'more']
        

class SessionForm(ModelForm):
    class Meta:
        model = SessionFeedback
        fields = ['sessionID', 'expectations', 'knowledge', 'knowledgeable', 'understandable', 'rightAmount', 'recommend', 'comments']
        