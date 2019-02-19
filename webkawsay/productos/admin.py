from django.contrib import admin
from .models import Producto, Categoria

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'description', 'category', 'price')
    search_fields = ('name', 'description', 'category__name')

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)