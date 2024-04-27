# Generated by Django 5.0.3 on 2024-04-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tally', '0029_alter_product_premature_alter_product_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Premature',
            field=models.CharField(choices=[('26-30', '26-30'), ('31-39', '31-39'), ('39', '39')], default='xxx', max_length=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='sex',
            field=models.CharField(choices=[('பெண்', 'பெண்'), ('ஆண்', 'ஆண்')], default='yyy', max_length=4),
        ),
    ]
