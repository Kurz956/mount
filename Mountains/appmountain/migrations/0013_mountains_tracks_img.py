# Generated by Django 5.0.2 on 2024-02-27 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmountain', '0012_mountains_prices_mountains_tracks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mountains',
            name='tracks_img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/', verbose_name='Схема трасс'),
        ),
    ]
