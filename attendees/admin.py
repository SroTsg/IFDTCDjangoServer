from django.contrib import admin

from attendees.models import Attendee


# Register your models here.
class AttendeeAdmin(admin.ModelAdmin):
    search_fields = ('firstname', 'lastname')

admin.site.register(Attendee, AttendeeAdmin)
