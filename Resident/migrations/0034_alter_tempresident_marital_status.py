# Generated by Django 4.0.2 on 2022-04-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0033_alter_resident_philhealth_membership_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempresident',
            name='Marital_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Separated', 'Separated'), ('Widowed', 'Widowed')], default='', max_length=100),
        ),
    ]
