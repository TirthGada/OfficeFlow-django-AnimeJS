# Generated by Django 4.1.7 on 2023-08-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='file',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
