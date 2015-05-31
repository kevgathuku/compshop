import factory
import factory.fuzzy

from store import models


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    name = factory.Sequence(lambda n: "Product_%d" % n)
    description = factory.fuzzy.FuzzyText()
    price = factory.fuzzy.FuzzyInteger(42000)
