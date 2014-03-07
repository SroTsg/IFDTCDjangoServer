from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ifdtc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('agenda.urls')),
    url(r'^', include('attendees.urls')),
    url(r'^', include('feedback.urls')),
    url(r'^', include('twitter.urls')),
    url(r'^', include('activities.urls'))
)
