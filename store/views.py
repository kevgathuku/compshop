from django.views.generic import DetailView, ListView

from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'store/index.html'


class ProductCatalogue(ListView):
    model = Product
    template_name = 'store/catalogue.html'


class ProductDetail(DetailView):
    model = Product
    pk_url_kwarg = 'product_id'
