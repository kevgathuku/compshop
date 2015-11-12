# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20151112_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(verbose_name='Image Name (optional)', max_length=200, blank=True),
        ),
    ]
