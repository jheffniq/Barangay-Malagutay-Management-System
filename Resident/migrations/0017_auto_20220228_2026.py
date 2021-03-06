# Generated by Django 3.2.9 on 2022-02-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0016_alter_resident_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='Blacklisted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resident',
            name='Marital_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Separated', 'Separated'), ('Widowed', 'Widowed')], default='', max_length=100),
        ),
    ]
