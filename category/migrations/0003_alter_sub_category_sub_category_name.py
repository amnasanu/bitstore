# Generated by Django 4.0.5 on 2022-07-03 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_sub_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_category',
            name='sub_category_name',
            field=models.CharField(max_length=50),
        ),
    ]
