# Generated by Django 3.0.3 on 2020-02-20 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emotions', '0005_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to=settings.AUTH_USER_MODEL),
        ),
    ]