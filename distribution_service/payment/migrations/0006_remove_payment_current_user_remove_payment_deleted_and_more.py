# Generated by Django 5.0.2 on 2024-02-14 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_alter_payment_amount_alter_payment_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='current_user',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='git_commit',
        ),
    ]
