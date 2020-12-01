# Generated by Django 3.1.3 on 2020-12-01 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0002_game_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('F', 'First Player to Move'), ('S', 'Second Player to Move'), ('W', 'First Player to Win'), ('L', 'Second Player to Win'), ('D', 'Draw')], default='F', max_length=1),
        ),
    ]