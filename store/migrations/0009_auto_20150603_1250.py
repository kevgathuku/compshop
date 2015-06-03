# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='misc',
            field=models.TextField(help_text='Additional info about the product', blank=True),
        ),
    ]
