# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 5, 29, 8, 56, 37, 111411, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(upload_to='%Y-%m-%d/'),
        ),
    ]
