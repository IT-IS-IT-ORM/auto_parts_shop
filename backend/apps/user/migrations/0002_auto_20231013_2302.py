# Generated by Django 3.2.8 on 2023-10-13 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'verbose_name': '收藏夹', 'verbose_name_plural': '收藏夹'},
        ),
        migrations.AlterModelTable(
            name='favorite',
            table='favorite',
        ),
    ]
