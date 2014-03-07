from django.conf.urls import patterns, url

urlpatterns = patterns('activities.views',
                       url(r'^activities', 'activity_list'),
                       url(r'^activitysubmit', 'ActivitySubmit')
)