'''
Created on Jan 27, 2014

@author: rfenton
'''
from rest_framework import serializers
from agenda.models import Event
from attendees.models import Attendee

class PresenterSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='jobtitle')
    
    class Meta:
        model = Attendee
        fields = ('firstname', 'lastname', 'title', 'bio')

class AgendaSerializer(serializers.ModelSerializer):
    Presenter = PresenterSerializer()
    date = serializers.DateField(source="date", format="%d-%b-%Y")

    class Meta:
        model = Event
        fields = ('id', 'title', 'date', 'starttime', 'endtime', 'room', 'track', 'level', 'Presenter', 'details')