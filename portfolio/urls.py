from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contacto', contacto, name='contacto'),
    path('post/<post_id>', post, name='post'),
    ]