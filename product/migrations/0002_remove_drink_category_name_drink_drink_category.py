# Generated by Django 4.0.5 on 2022-06-03 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='category_name',
        ),
        migrations.AddField(
            model_name='drink',
            name='drink_category',
            field=models.ManyToManyField(to='product.category'),
        ),
    ]
