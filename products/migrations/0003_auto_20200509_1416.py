# Generated by Django 2.2.7 on 2020-05-09 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200509_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='This is title', max_length=60),
        ),
    ]
