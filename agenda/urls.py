'''
Created on Jan 27, 2014

@author: rfenton
'''

from django.conf.urls import patterns, url

urlpatterns = patterns('agenda.views',
                       url(r'^agenda/$', 'agenda_list'),
                       url(r'^agenda/(?P<date>\S+)', 'agenda_detail')
)