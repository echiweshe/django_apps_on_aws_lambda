# To call the view, we need to map it to a URL - and for this we need a URLconf.
# To create a URLconf in the stats directory, create a file called urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]