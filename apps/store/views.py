from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    allmascota = mascota.objects.all()
    return render(request, 'index.html', {'allmascota':allmascota})

def Blog(request):
    return render(request, 'blog.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Petguide(request):
    return render(request, 'petguide.html')

def Petmart(request):
    return render(request, 'petmart.html')