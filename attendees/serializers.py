'''
Created on Jan 29, 2014

@author: rfenton
'''
from rest_framework import serializers
from attendees.models import Attendee

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ('firstname', 'lastname', 'nickname', "organization", "jobtitle", "department", "email")