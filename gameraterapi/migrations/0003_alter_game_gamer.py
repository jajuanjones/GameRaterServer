# Generated by Django 4.0.4 on 2022-05-10 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameraterapi', '0002_game_gamer_alter_game_designer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameraterapi.player'),
        ),
    ]
