from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from .forms import ReviewForm
from .models import Category, Product, Review


class CategoryDetail(DetailView):
    model = Category


class ProductList(ListView):
    model = Product
    template_name = 'store/index.html'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['featured'] = Product.objects.filter(featured=True)[:6]
        return context


class ProductCatalogue(ListView):
    model = Product
    template_name = 'store/catalogue.html'


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        context['main_image'] = self.object.images.first()
        context['specs'] = self.object.specs.all()
        context['reviews'] = self.object.reviews.all()
        context['form'] = ReviewForm(initial={'product': self.object})
        context['related'] = Product.objects.filter(
            category=self.object.category).exclude(id__exact=self.object.id)[:3]
        return context


def product_review(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReviewForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            product = form.cleaned_data['product']
            form.save()
            # redirect to a new URL:
            return redirect(
                reverse('products:detail', kwargs={'product_id': product.pk}))
    else:
        raise Http404
