from django.contrib import admin
from django.core import serializers

# Register your models here.
from agenda.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title','starttime')
    filter_horizontal = ('Presenter',)
    search_fields = ('title',)

admin.site.register(Event, EventAdmin)


