# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False, populate_from='name')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='%Y-%m-%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False, populate_from='name')),
                ('misc', models.TextField(blank=True, help_text='Additional info about the product')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=True)),
                ('category', models.ForeignKey(to='store.Category', related_name='products')),
                ('tags', taggit.managers.TaggableManager(blank=True, verbose_name='Tags', to='taggit.Tag', help_text='A comma-separated list of tags.', through='taggit.TaggedItem')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Anonymous', max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])),
                ('text', models.TextField()),
                ('product', models.ForeignKey(to='store.Product', related_name='reviews')),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('details', models.TextField()),
                ('product', models.ForeignKey(to='store.Product', related_name='specs')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ManyToManyField(related_name='images', to='store.Product'),
        ),
    ]
