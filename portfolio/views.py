from django.shortcuts import render, redirect, get_object_or_404
from .models import *
# Create your views here.
def home(request):
    galeria = Portfolio.objects.all()
    context={
        'galeria' : galeria
    }
    return render (request, 'main.html', context)


def contacto(request):
    return render (request, 'contacto.html')


def post(request, post_id):
    post = get_object_or_404(Portfolio, pk=post_id)



    context={
        'post' : post
    }
    return render (request, 'portfolio.html', context)