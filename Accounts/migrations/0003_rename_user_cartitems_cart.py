# Generated by Django 5.0.8 on 2024-08-10 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_cart_cartitems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitems',
            old_name='user',
            new_name='cart',
        ),
    ]
