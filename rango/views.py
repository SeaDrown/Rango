from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# okay!

def index(request):
    return HttpResponse("Rango says hey there partner!")

