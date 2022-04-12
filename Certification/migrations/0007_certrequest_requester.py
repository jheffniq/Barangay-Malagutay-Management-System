# Generated by Django 4.0.2 on 2022-04-06 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0021_delete_official'),
        ('Certification', '0006_certrequest_resident_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='certrequest',
            name='Requester',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Resident.resident'),
        ),
    ]