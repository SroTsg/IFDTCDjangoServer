from django.contrib import admin
from feedback.models import SessionFeedback, ConferenceFeedback

# Register your models here.

class SessionAdmin(admin.ModelAdmin):
    search_fields = ('sessionID',)

admin.site.register(SessionFeedback, SessionAdmin)
admin.site.register(ConferenceFeedback)