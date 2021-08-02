from django.shortcuts import render
from .models import *
# Create your views here.
def main(request):
    galeria = Portfolio.objects.all()

    context={
        'galeria' : galeria
    }
    return render (request, 'main.html', context)


def contacto(request):
    return render (request, 'contacto.html')


def portfolio(request):
    return render (request, 'portfolio.html')