from django.contrib import admin

from .models import Image, Product, Review, Specification


class ImageInline(admin.StackedInline):
    model = Image


class SpecificationInline(admin.StackedInline):
    model = Specification


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )
    inlines = [ImageInline, SpecificationInline, ]
    search_fields = ['name', 'description',]


class ReviewAdmin(admin.ModelAdmin):
    fields = ['product', 'name', 'title', 'rating', 'text']

admin.site.register(Image)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Specification)
