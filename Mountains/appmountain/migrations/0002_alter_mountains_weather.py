# Generated by Django 5.0.2 on 2024-02-22 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmountain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountains',
            name='weather',
            field=models.CharField(blank=True, default=0, max_length=500, verbose_name='Погода'),
        ),
    ]
