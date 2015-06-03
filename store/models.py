from django.db import models

from autoslug import AutoSlugField
from taggit.managers import TaggableManager


class Category(models.Model):
    """Represents the Category of a Product on Sale"""

    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Represents an Individual Product on Sale"""

    def category_default():
        obj, created = Category.objects.get_or_create(name='Laptops')
        return obj.id

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()

    category = models.ForeignKey(
        Category,
        related_name='products',
        default=category_default)

    misc = models.TextField(blank=True)
    tags = TaggableManager(blank=True)
    added = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=True)

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

    photo = models.ImageField(upload_to='%Y-%m-%d/')
    product = models.ManyToManyField(Product, related_name='images')

    def __str__(self):
        return self.photo.name


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
    title = models.CharField(max_length=50)
    rating = models.PositiveSmallIntegerField(choices=RATINGS_CHOICES, blank=False)
    text = models.TextField()
    product = models.ForeignKey(Product, related_name='reviews')

    def __str__(self):
        return '{} star: {}'.format(self.rating, self.title)
