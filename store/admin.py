from django.contrib import admin

from .models import Image, Product, Review, Specification


class ImageInline(admin.StackedInline):
    model = Image.product.through


class SpecificationInline(admin.StackedInline):
    model = Specification


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'featured',
    )
    inlines = [ImageInline, SpecificationInline, ]
    search_fields = ['name', 'description',]


class ReviewAdmin(admin.ModelAdmin):
    fields = ['product', 'name', 'title', 'rating', 'text']
    list_display = ('name','title','product','rating',)

admin.site.register(Image)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Specification)
