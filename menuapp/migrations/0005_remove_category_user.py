# Generated by Django 5.1.5 on 2025-02-13 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0004_offer_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
    ]
