from django.conf.urls import include, url
from .views import index,match
urlpatterns = [

    url(r'^$', index),
    url(r'^(?P<slug>\w+)', match),
]
