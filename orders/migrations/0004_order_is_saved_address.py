# Generated by Django 4.0.5 on 2022-07-13 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_payment_payment_signature_payment_razor_pay_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_saved_address',
            field=models.BooleanField(default=False),
        ),
    ]