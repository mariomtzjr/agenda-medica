# Generated by Django 2.2.1 on 2020-07-01 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='paciente',
        ),
    ]
