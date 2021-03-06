# Generated by Django 4.0.2 on 2022-02-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0009_alter_resident_address_alter_resident_vaccination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='Vaccination',
            field=models.CharField(choices=[('Vaccinated', 'Vaccinated'), ('Non-Vaccinated', 'Non-Vaccinated')], default='', max_length=100, verbose_name='Vaccination Status'),
        ),
    ]
