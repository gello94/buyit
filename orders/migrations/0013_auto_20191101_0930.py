# Generated by Django 2.2.6 on 2019-11-01 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20191026_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='voucher',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
    ]