# Generated by Django 3.0.7 on 2020-11-22 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201122_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provincia',
            name='province',
            field=models.CharField(default='', max_length=200, verbose_name='Province'),
        ),
    ]