from cloudinary.models import CloudinaryField

from django.core.urlresolvers import reverse
from django.db import models

from autoslug import AutoSlugField
from taggit.managers import TaggableManager


class Category(models.Model):
    """Represents the Category of a Product on Sale"""

    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse('category', args=[str(self.slug)])

    def __str__(self):
        return self.name


class Product(models.Model):
    """Represents an Individual Product on Sale"""

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    slug = AutoSlugField(populate_from='name', unique=True)
    category = models.ForeignKey(Category, related_name='products',)

    misc = models.TextField(
        blank=True,
        help_text='Additional info about the product')
    tags = TaggableManager(blank=True)
    added = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('products:detail', args=[str(self.slug)])

    def __str__(self):
        return self.name


class Specification(models.Model):
    """Represents the Product Details"""

    title = models.CharField(max_length=50)
    details = models.TextField()
    product = models.ForeignKey(Product, related_name='specs')

    def __str__(self):
        return self.title


class Image(models.Model):
    """Represents an Image associated with the Product"""

    title = models.CharField("Image Name (optional)",
                             max_length=200, blank=True)
    photo = CloudinaryField('photo')
    product = models.ManyToManyField(Product, related_name='images')

    def __str__(self):
        return self.photo.public_id


class Review(models.Model):
    """Reperesents a review of an individual product"""

    RATINGS_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )

    name = models.CharField(max_length=30, blank=True, default='Anonymous')
    rating = models.PositiveSmallIntegerField(
        choices=RATINGS_CHOICES, blank=False)
    text = models.TextField()
    product = models.ForeignKey(Product, related_name='reviews')

    def __str__(self):
        return '{} star: {}'.format(self.rating, self.product.name)
