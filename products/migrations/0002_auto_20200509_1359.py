# Generated by Django 2.2.7 on 2020-05-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.TextField(default='This is title'),
        ),
    ]
