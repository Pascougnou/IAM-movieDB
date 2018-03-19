from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<token>[a-zA-Z0-9\-]+)/*$', views.startPage, name='startPage'),
    url(r'', views.errorPage, name='errorPage'),
]
