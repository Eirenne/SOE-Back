# Generated by Django 3.0.3 on 2020-02-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotions', '0006_auto_20200220_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='date_time',
        ),
        migrations.AddField(
            model_name='record',
            name='date',
            field=models.DateField(default='2020-02-04'),
            preserve_default=False,
        ),
    ]
