from django.conf.urls import url

from .views import ProductCatalogue, ProductDetail, product_review


urlpatterns = [
    url(r'^catalogue/$', ProductCatalogue.as_view(), name='catalogue'),
    url(r'^(?P<slug>[\w\-]+)/$', ProductDetail.as_view(), name='detail'),
    url(r'^review/$', product_review, name='review'),
]
