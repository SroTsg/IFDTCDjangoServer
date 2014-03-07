'''
Created on Jan 29, 2014

@author: rfenton
'''
from django.conf.urls import patterns, url

urlpatterns = patterns('feedback.views',
                       url(r'^feedback/$', 'IFDTCEval'),
                       url(r'^sessionfeedback/$', 'SessionEval' )
)