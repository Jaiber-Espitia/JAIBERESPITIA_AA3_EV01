# Generated by Django 4.2.10 on 2024-03-07 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_tasksmanagement_is_finished_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksmanagement',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
