# Generated by Django 4.0.5 on 2022-08-26 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-03-03'),
            preserve_default=False,
        ),
    ]