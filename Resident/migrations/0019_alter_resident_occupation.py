# Generated by Django 4.0.2 on 2022-03-12 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0018_remove_resident_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='Occupation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]