# Generated by Django 2.2.6 on 2019-10-30 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0003_voucher_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voucher',
            name='price_reducing',
        ),
    ]
