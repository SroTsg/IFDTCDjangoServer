from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from attendees.models import Attendee
from attendees.serializers import AttendeeSerializer
from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
@xframe_options_exempt
def attendee_list(request):
    if request.method == 'GET':
        attenders = Attendee.objects.all()
        serializer = AttendeeSerializer(attenders, many=True)
        return JSONResponse(serializer.data)
 
@xframe_options_exempt 
def attendee_detail(request, letter):
    try:
        attenders = Attendee.objects.filter(lastname__startswith=letter)
    except Attendee.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = AttendeeSerializer(attenders)
        return JSONResponse(serializer.data)
