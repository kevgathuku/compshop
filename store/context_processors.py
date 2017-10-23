from django.conf import settings
from .models import Category, Product


def featured_products(request):
    """
    Returns a context variable containing featured products
    """
    return {'featured': Product.objects.filter(featured=True)[:9]}


def product_categories(request):
    """
    Returns a context variable containing categories with products
    """
    categories = [cat for cat in Category.objects.all()
                  if cat.products.count() > 0]
    return {'product_categories': categories}


def load_analytics(request):
    """
    Whether to load the Google Analytics tag or not
    """
    return {'load_analytics': settings.DEBUG == False}
