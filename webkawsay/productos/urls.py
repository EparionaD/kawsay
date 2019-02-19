from django.urls import path
from . import views

urlpatterns = [
    # Paths de productos
    path('', views.products, name="products"),
]
