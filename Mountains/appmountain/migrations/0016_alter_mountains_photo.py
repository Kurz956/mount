# Generated by Django 5.0.2 on 2024-02-28 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmountain', '0015_alter_mountains_photo_alter_mountains_season_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountains',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='<function Mountains.mountain_img_path at 0x000002B6E2A225C0>/logo.png', verbose_name='Фото'),
        ),
    ]
