'''
Created on Jan 29, 2014

@author: rfenton
'''
from django.conf.urls import patterns, url

urlpatterns = patterns('attendees.views',
                       url(r'^attendees/all', 'attendee_list'),
                       url(r'^attendees/(?P<letter>\S+)', 'attendee_detail')
)