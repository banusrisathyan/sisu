# Generated by Django 5.0.3 on 2024-04-23 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tally', '0051_alter_breastfeedingdetail_feelings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breastfeedingdetail',
            name='breastSide',
            field=models.CharField(choices=[('இடது', 'இடது'), ('வலது', 'வலது'), ('இரண்டும்', 'இரண்டும்'), ('இரண்டும் இல்லை', 'இரண்டும் இல்லை')], default='unknown', max_length=100),
        ),
    ]
