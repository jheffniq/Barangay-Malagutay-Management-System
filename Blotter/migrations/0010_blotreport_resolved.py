# Generated by Django 4.0.2 on 2022-05-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blotter', '0009_blotarchive'),
    ]

    operations = [
        migrations.AddField(
            model_name='blotreport',
            name='Resolved',
            field=models.BooleanField(default=False),
        ),
    ]
