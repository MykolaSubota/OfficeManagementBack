# Generated by Django 3.1.4 on 2021-06-22 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210614_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='timefixation',
            name='start',
            field=models.TimeField(auto_now_add=True, default='00:00:00', verbose_name='Початок'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timefixation',
            name='stop',
            field=models.TimeField(auto_now=True, verbose_name='Кінець'),
        ),
    ]