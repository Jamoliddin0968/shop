# Generated by Django 4.1.5 on 2023-02-25 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_product_characteristic_product_characteristic_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='characteristic',
        ),
        migrations.RemoveField(
            model_name='product',
            name='characteristic_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='characteristic_uz',
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.subcategory', verbose_name='Kategoriya'),
        ),
    ]
