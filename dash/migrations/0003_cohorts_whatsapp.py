# Generated by Django 4.0 on 2023-06-21 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_alter_payment_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='cohorts',
            name='whatsapp',
            field=models.CharField(blank=True, default='hello', max_length=400, null=True),
        ),
    ]