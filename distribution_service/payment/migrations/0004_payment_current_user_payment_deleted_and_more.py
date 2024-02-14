# Generated by Django 5.0.2 on 2024-02-14 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_cart_current_user_cart_deleted_cart_deleted_at_and_more'),
        ('payment', '0003_payment_processing_time_seconds'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='current_user',
            field=models.CharField(blank=True, max_length=63),
        ),
        migrations.AddField(
            model_name='payment',
            name='deleted',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AddField(
            model_name='payment',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='git_commit',
            field=models.CharField(blank=True, default='external', max_length=112),
        ),
        migrations.AlterUniqueTogether(
            name='payment',
            unique_together={('order', 'payment_id')},
        ),
    ]
