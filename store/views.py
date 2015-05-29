from django.views.generic import ListView

from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'store/index.html'


class ProductCatalogue(ListView):
    model = Product
    template_name = 'store/catalogue.html'
