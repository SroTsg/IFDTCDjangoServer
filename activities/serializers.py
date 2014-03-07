'''
Created on Feb 10, 2014

@author: rfenton
'''
from rest_framework import serializers
from activities.models import activity

class ActivitySerializer(serializers.ModelSerializer):
    dateString = serializers.DateField(source="date", format="%d-%b-%Y")
    timeString = serializers.TimeField(source="time", format="%I:%M %p")
    
    class Meta:
        model = activity
        fields = ('id', 'date', 'time', 'title', 'task', 'dateString', 'timeString')