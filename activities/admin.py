from django.contrib import admin

# Register your models here.

from activities.models import activity

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'date' ,'time')

admin.site.register(activity, ActivityAdmin)
