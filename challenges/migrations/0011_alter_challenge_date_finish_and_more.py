# Generated by Django 4.0.2 on 2022-03-13 12:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0010_alter_challenge_challenger_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='date_finish',
            field=models.DateField(default=datetime.datetime(2022, 3, 20, 12, 1, 27, 242289, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2022, 3, 13, 12, 1, 27, 242155, tzinfo=utc)),
        ),
    ]