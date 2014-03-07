from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from agenda.models import Event
from agenda.serializers import AgendaSerializer, PresenterSerializer
from django.views.decorators.clickjacking import xframe_options_exempt



# Create your views here.

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        
@csrf_exempt
@xframe_options_exempt
def agenda_list(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = AgendaSerializer(events, many=True)
        return JSONResponse(serializer.data)
    
@xframe_options_exempt    
def agenda_detail(request, date):
    try:
        events = Event.objects.filter(date=date)
    except Event.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = AgendaSerializer(events)
        return JSONResponse(serializer.data)
