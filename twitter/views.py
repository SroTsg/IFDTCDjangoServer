from django.shortcuts import render
from django.http import HttpResponse

from TwitterAPI import TwitterAPI

from django.views.decorators.clickjacking import xframe_options_exempt


import json
import datetime
# Create your views here.

@xframe_options_exempt
def twitter(request, search):
    consumer_key = ''
    consumer_secret = ''
    access_token_key = ''
    access_token_secret = ''
    
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    r = api.request('search/tweets', {'q':str(search)})
    data = json.loads(r.text)
    tweetInfo = '['
    for i in range(0,len(data['statuses'])):
        tweetInfo += '{'
        tweetInfo += '"id":"'+data['statuses'][i]['id_str']+'",'
        tweetInfo += '"avatar":"'+data['statuses'][i]['user']['profile_image_url']+'",'
        tweetInfo += '"tweetedOn":"'+data['statuses'][i]['created_at']+'",'
        tweetInfo += '"tweetedOnParsed":"'+datetime.datetime.strptime(data['statuses'][i]['created_at'], "%a %b %d %X %z %Y").strftime("%X")+'",'
        tweetInfo += '"screenname":"'+data['statuses'][i]['user']['screen_name']+'",'
        tweetInfo += '"status":"'+data['statuses'][i]['text'].replace('"',"'").replace('\n','').replace('\r','')+'",'
        tweetInfo += '"truncated":"'+str(data['statuses'][i]['truncated'])+'",'
        tweetInfo += '"retweeted":"'+str(data['statuses'][1]['retweeted'])+'"'
        tweetInfo += '}'
        if i+1 < len(data['statuses']):
            tweetInfo += ','
    tweetInfo += ']'
        
    
    return HttpResponse(tweetInfo)
    
