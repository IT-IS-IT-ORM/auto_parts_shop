# Generated by Django 3.2.8 on 2023-12-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('sm', 'Жеңіл автомобил'), ('md', 'Фургон'), ('lg', 'Үлкен жүк көлік')], max_length=2, verbose_name='商品类型'),
        ),
    ]