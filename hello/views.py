from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    #return HttpResponse('<b>Hello, World!</b>')
    return render(request, 'cover.html')

def home(request, numcols = 18):
    my_col_range = range(0, int(numcols))
    return render(request, 'StarterBootstrap.html', {'home_col_text': "Hello, Django!", 'my_col_range': my_col_range})

def carousel(request):
    return render(request, 'carousel.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

