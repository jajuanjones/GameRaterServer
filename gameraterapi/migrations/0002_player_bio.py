# Generated by Django 4.0.4 on 2022-05-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameraterapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='bio',
            field=models.TextField(default=None),
        ),
    ]