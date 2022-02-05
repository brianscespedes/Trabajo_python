# Generated by Django 4.0.2 on 2022-02-05 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_program_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='backend.professor', verbose_name='Profesor'),
        ),
    ]