# Generated by Django 5.0.2 on 2024-02-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmountain', '0004_resort_slug_alter_mountains_resort_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mountains',
            name='link',
            field=models.TextField(blank=True, default='', verbose_name='Линк'),
        ),
    ]
