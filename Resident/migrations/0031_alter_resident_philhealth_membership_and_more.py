# Generated by Django 4.0.2 on 2022-04-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0030_alter_resident_philhealth_membership_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='Philhealth_membership',
            field=models.CharField(choices=[('Sponsored', 'Sponsored'), ('OFW', 'OFW'), ('Employed', 'Employed'), ('Lifetime', 'Lifetime'), ('Indigent', 'Indigent'), ('Senior', 'Senior'), ('Voluntary', 'Voluntary')], default='None', max_length=100, verbose_name='Philhealth Membership Type'),
        ),
        migrations.AlterField(
            model_name='tempresident',
            name='Philhealth_membership',
            field=models.CharField(choices=[('Sponsored', 'Sponsored'), ('OFW', 'OFW'), ('Employed', 'Employed'), ('Lifetime', 'Lifetime'), ('Indigent', 'Indigent'), ('Senior', 'Senior'), ('Voluntary', 'Voluntary'), ('None', 'None')], default='None', max_length=100, verbose_name='Philhealth Membership Type'),
        ),
    ]