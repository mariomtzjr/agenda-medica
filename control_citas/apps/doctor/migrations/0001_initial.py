# Generated by Django 2.2 on 2020-05-26 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('comentario', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='paciente.Paciente')),
            ],
            options={
                'verbose_name': 'doctor',
                'verbose_name_plural': 'doctores',
            },
        ),
    ]
