# Generated by Django 4.0.2 on 2022-03-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_applicant_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recruit',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]