from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('contacto', contacto, name='contacto'),
    path('portfolio', portfolio, name='portfolio'),
    ]