from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from .models import Category, Product, Review


class CategoryDetail(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['categories'] = [cat for cat in Category.objects.all()
                                 if cat.products.count() > 0]
        return context


class ProductList(ListView):
    model = Product
    template_name = 'store/index.html'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['featured'] = Product.objects.filter(featured=True)[:6]
        context['categories'] = [cat for cat in Category.objects.all()
                                 if cat.products.count() > 0]
        return context


class ProductCatalogue(ListView):
    model = Product
    template_name = 'store/catalogue.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCatalogue, self).get_context_data(**kwargs)
        context['categories'] = [cat for cat in Category.objects.all()
                                 if cat.products.count() > 0]
        return context


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        context['main_image'] = self.object.images.first()
        context['specs'] = self.object.specs.all()
        context['reviews'] = self.object.reviews.all()
        context['related'] = Product.objects.filter(
            category=self.object.category).exclude(
            id__exact=self.object.id)[:3]
        return context


def product_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        text = request.POST.get('text')
        prod = request.POST.get('product')
        if name and rating and text and prod:
            product = Product.objects.get(id=prod)
            review = Review.objects.create(name=name, rating=rating, text=text, product=product)
            review.full_clean()
            return redirect(product)
    else:
        raise Http404
