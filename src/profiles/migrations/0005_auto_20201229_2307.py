# Generated by Django 3.1.4 on 2020-12-29 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20201229_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='middle_name',
            field=models.CharField(max_length=50, verbose_name='По-батькові'),
        ),
    ]