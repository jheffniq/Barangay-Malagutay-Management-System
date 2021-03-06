# Generated by Django 3.2.9 on 2022-02-20 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Middle_name', models.CharField(max_length=50)),
                ('Birthdate', models.DateField()),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Not Specified', max_length=100)),
                ('Contact', models.CharField(max_length=11)),
                ('Citizenship', models.CharField(max_length=100)),
                ('Religion', models.CharField(max_length=100)),
                ('Occupation', models.CharField(max_length=100)),
                ('Vaccination', models.CharField(choices=[('Vaccinated', 'Vaccinated'), ('Non-Vaccinated', 'Non-Vaccinated')], default='', max_length=100)),
                ('Address', models.TextField(max_length=250)),
            ],
        ),
    ]
