# Generated by Django 5.0.2 on 2024-02-11 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_rename_amount_fee_payment_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='processing_time_seconds',
            field=models.FloatField(default=5),
        ),
    ]