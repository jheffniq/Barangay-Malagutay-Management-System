# Generated by Django 4.0.2 on 2022-04-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0031_alter_resident_philhealth_membership_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='Philhealth_membership',
            field=models.CharField(choices=[('Indigent', 'Indigent'), ('Senior', 'Senior'), ('Employed', 'Employed'), ('Voluntary', 'Voluntary'), ('None', 'None'), ('Sponsored', 'Sponsored'), ('Lifetime', 'Lifetime'), ('OFW', 'OFW')], default='None', max_length=100, verbose_name='Philhealth Membership Type'),
        ),
        migrations.AlterField(
            model_name='tempresident',
            name='Philhealth_membership',
            field=models.CharField(choices=[('Indigent', 'Indigent'), ('Senior', 'Senior'), ('Employed', 'Employed'), ('Voluntary', 'Voluntary'), ('None', 'None'), ('Sponsored', 'Sponsored'), ('Lifetime', 'Lifetime'), ('OFW', 'OFW')], default='None', max_length=100, verbose_name='Philhealth Membership Type'),
        ),
    ]
