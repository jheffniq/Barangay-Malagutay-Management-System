# Generated by Django 4.0.2 on 2022-05-18 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0045_remove_household_member_household_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='household',
            name='Members',
        ),
        migrations.AddField(
            model_name='household',
            name='HMembers',
            field=models.ManyToManyField(to='Resident.Resident'),
        ),
    ]
