# Generated by Django 5.0.2 on 2024-02-10 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='amount_fee',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='amount_gross',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='amount_net',
        ),
    ]
