# Generated by Django 2.2.6 on 2019-10-25 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
