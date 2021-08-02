from django.contrib import admin
from .models import *

# Register your models here.



class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', ) #visualizar columnas




admin.site.register(Portfolio, PortfolioAdmin)