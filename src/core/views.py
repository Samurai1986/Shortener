from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Shortener
from django.contrib.sites.shortcuts import get_current_site
import random, string, re
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.

import json

# @csrf_exempt
def urls(request, shorturl=None):
    context = {}
    if request.method == 'POST': #savelink
        # response = print(request.POST.itervalues()) #валим джанго чтобы видеть поля поста
        link = request.POST.get('linkresolver', '')
        # link = request.POST.get('linkresolver','[]')
        match = re.match(r'https?://', link) #возвращает совпадение
        if not match: #False лень менять местами, поэтому not
            error =  "отсутствует http:// или https://"
            context.update({"error": error}) # {% if response %} <p>{{response}}</p> {% endif %}
            return json.dumps(error)
        else: #regex это объект с 7 символами поэтому True
            shlink = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(Shortener.length))
            shortener = Shortener(link=link, shlink=shlink)
            shortener.save()
            # site = str( get_current_site(request))
            site = "localhost"
            response = "http://"+site+"/"+shortener.shlink
            context.update({'response': response}) # {% if response %} <p>{{response}}</p> {% endif %}
            # return json.dumps(response)
            return HttpResponse(json.dumps({'response': response})) 

            # return render(request, 'core\index.html', context)
    else:
        if shorturl:
            try:
                shortener = Shortener.objects.get(shlink=shorturl)
                return HttpResponseRedirect(shortener.link)
            except Shortener.DoesNotExist:
                context.update({'error': u'Данный URL не найден'}) # {% if error %} <p>{{error}}</p> {% endif %}
                return render(request, 'core/index.html', context)
        else:
            return render(request, 'core/index.html', context)
