# Generated by Django 4.0.2 on 2022-04-14 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blotter', '0007_alter_blotreport_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blotreport',
            name='Offender_unregistered',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Offender'),
        ),
    ]
