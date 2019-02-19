from django.shortcuts import render
from .models import Producto

# Create your views here.
def products(request):
    traditionals = Producto.objects.all().filter(category_id = 1)
    medicinals = Producto.objects.all().filter(category_id = 2)
    return render(request, "productos/productos.html", {'traditionals':traditionals, 'medicinals':medicinals})