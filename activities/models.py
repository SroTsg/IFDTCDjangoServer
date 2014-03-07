from django.db import models
from django.forms import ModelForm

# Create your models here.

class activity(models.Model):
    date = models.DateField()
    time = models.TimeField()
    title = models.CharField(max_length=1000)
    task = models.TextField()
    
    def __str__(self):
        return self.title
    
class activityForm(ModelForm):
    class Meta:
        model = activity
        fields = ['date', 'time', 'title', 'task']
