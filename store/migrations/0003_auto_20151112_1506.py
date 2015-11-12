# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20150605_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='photo'),
        ),
    ]
