# Generated by Django 2.2.5 on 2020-01-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.PositiveIntegerField()),
                ('game_round', models.PositiveIntegerField()),
                ('user_id', models.CharField(max_length=20)),
                ('balance', models.PositiveIntegerField()),
                ('bet_red', models.PositiveIntegerField()),
                ('bet_white', models.PositiveIntegerField()),
            ],
        ),
    ]
