from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.urls),
    # url(r'^new/$', views.urls),
    # url(r'^(?P<shorturl>[0-9, A-Z]{5,7})$', views.urls),
]
