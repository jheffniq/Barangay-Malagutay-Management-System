# Generated by Django 4.0.2 on 2022-04-30 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0040_alter_resident_contact_alter_tempresident_contact'),
        ('Blotter', '0008_alter_blotreport_offender_unregistered'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlotArchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Offender_unregistered', models.CharField(blank=True, max_length=50, null=True, verbose_name='Offender')),
                ('Complainant', models.CharField(max_length=50)),
                ('Complaint', models.TextField(max_length=1000)),
                ('Facts', models.TextField(max_length=250)),
                ('Unregistered', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('Offender', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Resident.resident')),
            ],
        ),
    ]
