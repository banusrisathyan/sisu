# Generated by Django 5.0.3 on 2024-04-06 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tally', '0004_alter_userinfo_date_of_birth_alter_userinfo_pregnant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
    ]
