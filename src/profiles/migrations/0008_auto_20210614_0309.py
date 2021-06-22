# Generated by Django 3.1.4 on 2021-06-14 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20210612_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='middle_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='По-батькові'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='phone',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name=' Номер телефону'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='position',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Посада'),
        ),
    ]