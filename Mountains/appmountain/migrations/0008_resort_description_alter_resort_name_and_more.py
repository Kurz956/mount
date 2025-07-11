# Generated by Django 5.0.2 on 2024-02-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmountain', '0007_alter_tagmountain_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='resort',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='resort',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='resort',
            name='stars',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Рейтинг инфраструктуры'),
        ),
    ]
