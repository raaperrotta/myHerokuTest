from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    #return HttpResponse('<b>Hello, World!</b>')
    return render(request, 'cover.html')

def home(request):
    return render(request, 'StarterBootstrap.html')

def carousel(request):
    return render(request, 'carousel.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

