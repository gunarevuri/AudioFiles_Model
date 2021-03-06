# Generated by Django 3.2 on 2021-04-22 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiobook',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='audiobook',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='podcast',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='podcast',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='song',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='song',
            name='created_on',
        ),
        migrations.AlterField(
            model_name='audiobook',
            name='Upload_Time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='Upload_Time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='song',
            name='Upload_Time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
