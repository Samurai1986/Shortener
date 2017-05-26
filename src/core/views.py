from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Shortener
from django.contrib.sites.shortcuts import get_current_site
import random, string
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

import json

@csrf_exempt
def urls(request, shorturl=None):
    context = {}
    if request.method == 'POST': #savelink
        print(request.POST.get("url"))
        # link = json.loads(request.POST.get('url','[]'))

        # shlink = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(Shortener.length))
        # shortener = Shortener(link=link, shlink=shlink)
        # shortener.save()
        # return json.dumps(shortener)
        # response = get_current_site(request)+"/"+shortener.shlink
        # context.update({'response': u'Данный URL не найден'}) # {% if response %} <p>{{response}}</p> {% endif %}
        # return render(request, 'core\index.html', context)
    else:
        if shorturl:
            try:
                shortener = Shortener.objects.get(shlink=shorturl)
                return HttpResponseRedirect(shortener.link)
            except Shortener.DoesNotExist:
                context.update({'error': u'Данный URL не найден'}) # {% if error %} <p>{{error}}</p> {% endif %}
                return render(request, 'core\index.html', context)
        else:
            return render(request, 'core\index.html', context)
