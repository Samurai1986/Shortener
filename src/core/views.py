#from django.shortcuts import render
from django.http import HttpResponse
from .models import Shortener
from django.contrib.sites.shortcuts import get_current_site
import random, string
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def urls(request):
    if request.method == 'POST': #savelink
        print(request)
        Shortener.link = request
        Shortener.shlink = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(Shortener.length)) #random code generator
        Shortener.save
        response  = get_current_site(request),"/",Shortener.shlink
        return HttpResponse(response)
    elif request.method == 'GET': #returnlink
        print('it\'s get')
        return HttpResponse('it\'s get')

        #
        #self.save

#def returnlink(request):
#    if request.path == Shortener.shlink:
#        return Shortener.link
