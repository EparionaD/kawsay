from django.shortcuts import render
from .models import Producto

# Create your views here.
def products(request):
    traditionals = Producto.objects.all().filter(category_id = 1)
    fruts = Producto.objects.all().filter(category_id = 2)
    medicinals = Producto.objects.all().filter(category_id = 3)
    combinations = Producto.objects.all().filter(category_id = 4)
    return render(request, "productos/productos.html", {'traditionals':traditionals, 'fruts':fruts, 'medicinals':medicinals, 'combinations':combinations})