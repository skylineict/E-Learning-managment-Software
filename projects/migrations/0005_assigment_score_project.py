# Generated by Django 4.0 on 2023-10-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_ending_date_alter_project_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='assigment',
            name='score_project',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]