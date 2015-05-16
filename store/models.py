from django.db import models

from taggit.managers import TaggableManager


class Product(models.Model):
    """Represents an Individual Product on Sale"""

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    misc = models.TextField(blank=True)
    tags = TaggableManager(blank=True)

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
    product = models.ForeignKey(Product, related_name='images')

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

    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    rating = models.IntegerField(choices=RATINGS_CHOICES)
    text = models.TextField()
    product = models.ForeignKey(Product, related_name='reviews')

    def __str__(self):
        return self.title
