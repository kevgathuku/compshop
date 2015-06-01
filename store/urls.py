from django.conf.urls import url

from .views import ProductCatalogue, ProductDisplay


urlpatterns = [
    url(r'^catalogue/$', ProductCatalogue.as_view(), name='catalogue'),
    url(r'^(?P<product_id>[0-9]+)/$', ProductDisplay.as_view(), name='detail'),
]
