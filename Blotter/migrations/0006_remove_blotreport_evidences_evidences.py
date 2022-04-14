# Generated by Django 4.0.2 on 2022-04-13 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blotter', '0005_blotreport_evidences'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blotreport',
            name='Evidences',
        ),
        migrations.CreateModel(
            name='Evidences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
                ('Report', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Blotter.blotreport')),
            ],
        ),
    ]
