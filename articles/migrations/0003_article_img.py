# Generated by Django 5.0.7 on 2024-08-01 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_categories_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.URLField(default='', verbose_name='Image'),
        ),
    ]
