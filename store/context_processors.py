from .models import Category


def footer_categories(request):
    """
    Returns a context variable containing all categories
    """
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}
