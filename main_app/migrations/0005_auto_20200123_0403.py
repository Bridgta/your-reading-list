# Generated by Django 2.2.9 on 2020-01-23 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200123_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='bookmark',
            field=models.CharField(max_length=150),
        ),
    ]
