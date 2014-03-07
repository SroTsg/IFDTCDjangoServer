'''
Created on Feb 5, 2014

@author: rfenton
'''
from django.conf.urls import patterns, url

urlpatterns = patterns('twitter.views',
                       url(r'^twitter/(?P<search>\S+)', 'twitter')
)