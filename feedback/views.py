from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from feedback.models import ConferenceForm, SessionForm, ConferenceFeedback, SessionFeedback
from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.
@csrf_exempt
@xframe_options_exempt
def IFDTCEval(request):
    if request.method == 'POST':
        conform = ConferenceForm(request.POST)
        if conform.is_valid():
            conform.save()
        return HttpResponse('IFDTCEval Posted')
    if request.method == 'GET':
        return HttpResponse('Get IFDTCEval GET!')
            
@csrf_exempt 
@xframe_options_exempt
def SessionEval(request):
    if request.method == 'POST':
        seshform = SessionForm(request.POST)
        if seshform.is_valid():
            seshform.save()
        return HttpResponse('SessionEval Posted')
    if request.method == 'GET':
        return HttpResponse('Get SessionEval GET!')