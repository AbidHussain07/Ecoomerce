# Generated by Django 5.0.8 on 2024-08-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_colourvariant_sizevariant_product_colour_variant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colourvariant',
            name='colour',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sizevariant',
            name='size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]