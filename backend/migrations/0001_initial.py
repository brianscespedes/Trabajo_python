# Generated by Django 4.0.2 on 2022-02-03 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, verbose_name='nombre')),
                ('is_active', models.BooleanField(default=True, verbose_name='activo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, verbose_name='nombre')),
                ('is_active', models.BooleanField(default=True, verbose_name='activo')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to='backend.building')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
