# Generated by Django 3.2 on 2021-05-21 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20210520_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
    ]
