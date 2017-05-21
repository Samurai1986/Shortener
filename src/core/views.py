from django.shortcuts import render
from django.http import HttpResponse
from .models import Shortener
import random, string
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def urls(request):
    if request.method == 'POST': #savelink
        print("it's post")
        return HttpResponse("it\'s post")
    elif request.method == 'GET': #returnlink
        print('it\'s get')
        return HttpResponse('it\'s get')

        #self.shlink = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(Shortener.shlink.max_length)) #random code generator
        #self.save

#def returnlink(request):
#    if request.path == Shortener.shlink:
#        return Shortener.link
