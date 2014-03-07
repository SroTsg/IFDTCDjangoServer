from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from activities.models import activity, activityForm
from activities.serializers import ActivitySerializer
from django.views.decorators.clickjacking import xframe_options_exempt


import datetime


# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        
@csrf_exempt
def activity_list(request):
    if request.method == 'GET':
        events = activity.objects.filter(date__gte=datetime.date.today()).order_by('date', 'time')
        serializer = ActivitySerializer(events, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
@xframe_options_exempt
def ActivitySubmit(request):
    if request.method == 'POST':
        seshform = activityForm(request.POST)
        if seshform.is_valid():
            seshform.save()
        return HttpResponse('ActivitySubmit Posted')
    if request.method == 'GET':
        return HttpResponse('Get ActivitySubmit GET!')
