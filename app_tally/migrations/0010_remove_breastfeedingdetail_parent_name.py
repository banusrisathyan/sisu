# Generated by Django 5.0.3 on 2024-04-15 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tally', '0009_breastfeedingdetail_parent_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breastfeedingdetail',
            name='parent_Name',
        ),
    ]
