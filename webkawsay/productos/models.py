from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Nombre de categoría")
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creacción")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de modificación")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Producto(models.Model):

    name = models.CharField(max_length=200, verbose_name = "Nombre del producto")
    description = RichTextField(verbose_name = "Descripción del producto")
    image = models.ImageField(verbose_name = "Imagen del producto", upload_to = "productos")
    category = models.ForeignKey(Categoria, on_delete = models.CASCADE, verbose_name = "Categoría")
    price = models.DecimalField(max_digits = 4, decimal_places = 2, verbose_name = "Precio del Producto")
    link = models.URLField(null= True, blank = True, verbose_name = "Enlace para compra")
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creacción")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de modificación")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ['-created']

    def __str__(self):
        return self.name
