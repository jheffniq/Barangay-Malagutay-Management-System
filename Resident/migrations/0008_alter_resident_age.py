# Generated by Django 4.0.2 on 2022-02-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0007_alter_resident_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='Age',
            field=models.IntegerField(),
        ),
    ]
