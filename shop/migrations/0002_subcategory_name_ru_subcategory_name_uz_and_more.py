# Generated by Django 4.0.6 on 2023-02-14 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='name_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Subkategoriya nomi'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_uz',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Subkategoriya nomi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.subcategory', verbose_name='SubKategoriya'),
        ),
    ]
