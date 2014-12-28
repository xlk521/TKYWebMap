#coding=utf8
'''
Created on 2014年7月18日

@author: Derek Xie
'''

from datetime import *
import time
from django.shortcuts import render_to_response, render 
from django.template.context import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import UdpMap

def convertjson(result):
    try:
        result =  json.dumps(result, ensure_ascii=False, separators=(',',':'), cls = DjangoJSONEncoder)
    except Exception as e:
        print(e)
    return result

def map(request):
    if request.method == 'POST':
#         list = UdpMap.object.all()
        dt = datetime.now() - timedelta(minutes=30)
        tNow = dt.strftime('%Y-%m-%d %H:%M:%S')
        list = UdpMap.object.filter(time__gte=tNow)
        getwork = []
        for l in list:
            print l.user_id
            try:
                work = {}
                work['user_id'] = l.user_id
                work['dept'] = l.dept
                work['time'] = l.time
                work['lat'] = l.lat
                work['lng'] = l.lng
                work['checi'] = l.checi
                print 'getwork:'
                getwork.append(work)
                print getwork
            except:
                print 'map;err'
                return
#         return HttpResponse(getwork, mimetype='application/javascript')
        return HttpResponse(convertjson(getwork))
    else:
        return render_to_response('map\map.html', context_instance=RequestContext(request))