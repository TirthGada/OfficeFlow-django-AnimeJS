# Generated by Django 4.1.7 on 2023-08-26 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('office', '0008_team_employee_teamname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateField()),
                ('completion_date', models.DateField()),
                ('task_desc', models.CharField(max_length=500)),
                ('status', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('team', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='office.team')),
            ],
        ),
    ]