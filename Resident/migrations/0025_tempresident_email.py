# Generated by Django 4.0.2 on 2022-04-11 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0024_tempresident'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempresident',
            name='Email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]