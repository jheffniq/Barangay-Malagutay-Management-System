# Generated by Django 4.0.2 on 2022-04-13 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blotter', '0004_blotreport_unregistered'),
    ]

    operations = [
        migrations.AddField(
            model_name='blotreport',
            name='Evidences',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
