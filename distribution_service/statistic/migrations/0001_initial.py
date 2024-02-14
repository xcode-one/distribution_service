# Generated by Django 5.0.2 on 2024-02-10 11:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ice_cream', '0003_icecream_flavor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EndpointPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint', models.CharField(max_length=255)),
                ('response_time', models.FloatField(help_text='Response time in seconds')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('ice_cream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_statistic', to='ice_cream.icecream')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_statistic', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('successful', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('failure_reason', models.TextField(blank=True, null=True)),
                ('processing_time_seconds', models.FloatField()),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='statistic.order')),
            ],
        ),
    ]