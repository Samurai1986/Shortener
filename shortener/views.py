from django.shortcuts import render
from django.http import HttpResponse
from .models import Shortener
import random, string
# Create your views here.
def savelink(request):
        self.shlink = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(Shortener.shlink.max_length)) #random code generator
        self.save

def returnlink(request):
    if request.path == Shortener.shlink:
        return Shortener.link
