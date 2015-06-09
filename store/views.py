from django.http import Http404, JsonResponse
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from .forms import ReviewForm
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
        context['form'] = ReviewForm(initial={'product': self.object})
        context['related'] = Product.objects.filter(
            category=self.object.category).exclude(
            id__exact=self.object.id)[:3]
        return context


def product_review(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Save the form data
            form.save()
            return JsonResponse(
                {"reviewRating": "", "reviewName": "", "reviewText": ""})
        else:
            if 'rating' in form.errors:
                return JsonResponse(
                    {"reviewName": "", "reviewRating": form.errors['rating'][0], "reviewText": ""})
            elif 'name' in form.errors:
                return JsonResponse(
                    {"reviewRating": "", "reviewName": form.errors['name'][0], "reviewText": ""})
            elif 'text' in form.errors:
                return JsonResponse(
                    {"reviewName": "", "reviewRating": "", "reviewText": form.errors['text'][0]})
    else:
        raise Http404
