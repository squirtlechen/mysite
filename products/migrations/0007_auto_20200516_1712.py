# Generated by Django 2.2.7 on 2020-05-16 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200516_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='summery',
            new_name='summary',
        ),
    ]
