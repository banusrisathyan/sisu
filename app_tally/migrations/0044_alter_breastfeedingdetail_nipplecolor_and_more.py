# Generated by Django 5.0.3 on 2024-04-23 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tally', '0043_alter_breastfeedingdetail_breastside'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breastfeedingdetail',
            name='nippleColor',
            field=models.CharField(choices=[('கருப்பு நிறம்', 'கருப்பு நிறம்'), ('வெள்ளை நிறம்', 'வெள்ளை நிறம்'), ('சிவப்பு நிறம்', 'சிவப்பு நிறம்')], max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeedingdetail',
            name='nippleShape',
            field=models.CharField(choices=[('வட்ட வடிவ முலைக்காம்பு', 'வட்ட வடிவ முலைக்காம்பு'), ('கூம்புவடிவ முலைக்காம்பு', 'கூம்புவடிவ முலைக்காம்பு')], max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeedingdetail',
            name='supplement',
            field=models.CharField(choices=[('தாய்ப்பால்', 'தாய்ப்பால்'), ('பவுடர்பால்', 'பவுடர்பால்')], max_length=20),
        ),
    ]
