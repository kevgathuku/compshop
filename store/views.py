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

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        context['main_image'] = self.object.images.first()
        return context
