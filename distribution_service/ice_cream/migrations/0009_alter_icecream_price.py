# Generated by Django 5.0.2 on 2024-02-14 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0008_alter_icecream_flavor_alter_icecream_uuid_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecream',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Product price', max_digits=5),
        ),
    ]
