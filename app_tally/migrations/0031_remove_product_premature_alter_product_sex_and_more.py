# Generated by Django 5.0.3 on 2024-04-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tally', '0030_alter_product_premature_alter_product_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Premature',
        ),
        migrations.AlterField(
            model_name='product',
            name='sex',
            field=models.CharField(choices=[('பெண்', 'பெண்'), ('ஆண்', 'ஆண்')], default='girl', max_length=4),
        ),
        migrations.AddField(
            model_name='product',
            name='premature',
            field=models.CharField(choices=[('26-30', '26-30'), ('31-39', '31-39'), ('39', '39')], default='26-30', max_length=6),
        ),
    ]
