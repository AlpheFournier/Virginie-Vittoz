from django.shortcuts import render, loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('Accueil.html')
    return HttpResponse(template.render(request=request))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render(request=request))


# Create your views here.
