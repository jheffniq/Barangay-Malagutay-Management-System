# Generated by Django 3.2.9 on 2022-03-03 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0017_auto_20220228_2026'),
        ('Blotter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blotreport',
            name='Offender',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Resident.resident'),
        ),
    ]
