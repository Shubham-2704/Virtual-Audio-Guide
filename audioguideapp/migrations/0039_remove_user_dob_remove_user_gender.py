# Generated by Django 4.1.3 on 2023-03-21 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audioguideapp', '0038_payment_monument_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
    ]
