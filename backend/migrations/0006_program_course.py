# Generated by Django 4.0.2 on 2022-02-03 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_student_alter_professortype_options_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, verbose_name='nombre')),
                ('is_active', models.BooleanField(default=True, verbose_name='activo')),
            ],
            options={
                'verbose_name': 'programa',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, verbose_name='nombre')),
                ('is_active', models.BooleanField(default=True, verbose_name='activo')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.program', verbose_name='programa')),
            ],
            options={
                'verbose_name': 'curso',
            },
        ),
    ]
