from django.http import Http404, JsonResponse
from django.views.generic import DetailView, ListView, TemplateView

from .forms import ReviewForm
from .models import Category, Product


class AboutView(TemplateView):
    """This handles the 'About Us' page"""

    template_name = "store/about.html"


class ContactView(TemplateView):
    """This handles the 'Contact Us' page"""

    template_name = "store/contact.html"


class CategoryDetail(DetailView):
    model = Category


class ProductList(ListView):
    model = Product
    template_name = 'store/index.html'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['latest'] = Product.objects.order_by('-added')[:3]
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
            response = {"reviewRating": "", "reviewName": "", "reviewText": ""}
            if 'rating' in form.errors:
                response["reviewRating"] = form.errors['rating'][0]
            if 'name' in form.errors:
                response["reviewName"] = form.errors['name'][0]
            if 'text' in form.errors:
                response["reviewText"] = form.errors['text'][0]
            return JsonResponse(response)
    else:
        raise Http404
