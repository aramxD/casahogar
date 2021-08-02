from django.db import models

# Create your models here.
class Portfolio(models.Model):
    #Datos generales
    titulo = models.CharField(max_length=30)
    alt = models.CharField(max_length=30)
    descripcion  = models.CharField(max_length=150)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="images/posts", blank=True)
    
    def __str__(self):
        return self.titulo