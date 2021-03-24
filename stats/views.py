from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# This is the simplest view possible in Django
def index(request):
    return HttpResponse("<h1>Descriptive Statistics Calculator</h1>")