# Generated by Django 4.0.2 on 2022-02-21 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0012_resident_created_date_resident_modified_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resident',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='resident',
            name='modified_date',
        ),
    ]
