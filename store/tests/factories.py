import factory
import factory.fuzzy

from store import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Sequence(lambda n: "Category_%d" % n)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    name = factory.Sequence(lambda n: "Product_%d" % n)
    description = factory.fuzzy.FuzzyText()
    price = factory.fuzzy.FuzzyInteger(42000)
    category = factory.SubFactory(CategoryFactory)


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Review

    name = factory.Sequence(lambda n: "Reviewer_%d" % n)
    rating = factory.fuzzy.FuzzyChoice(dict(models.Review.RATINGS_CHOICES).keys())
    text = factory.fuzzy.FuzzyText()
    product = factory.SubFactory(ProductFactory)
