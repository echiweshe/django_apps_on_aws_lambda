from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# This is the simplest view possible in Django
def index(request):
    return HttpResponse("Hello ASHLYNE CHIWESHE. \n You're at the your father's statistics calculator page. This is added")