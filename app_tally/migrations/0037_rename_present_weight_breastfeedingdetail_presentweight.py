# Generated by Django 5.0.3 on 2024-04-22 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tally', '0036_remove_breastfeedingdetail_breastside_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='breastfeedingdetail',
            old_name='present_weight',
            new_name='presentWeight',
        ),
    ]
