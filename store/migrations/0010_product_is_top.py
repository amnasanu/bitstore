# Generated by Django 4.0.5 on 2022-07-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_carousel_is_featured_carousel_is_top_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_top',
            field=models.BooleanField(default=False),
        ),
    ]