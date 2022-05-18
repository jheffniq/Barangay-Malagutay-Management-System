# Generated by Django 4.0.2 on 2022-05-18 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0042_household_contact_household_homeowner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='Income',
            field=models.CharField(choices=[('131,000 and up', '131,000 and up'), ('41,000 - 130,000', '41,000 - 130,000'), ('11,000 - 40,000', '11,000 - 40,000'), ('Less than 10,000', 'Less than 10,000')], default='', max_length=250),
        ),
    ]
