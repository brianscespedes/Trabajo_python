# Generated by Django 4.0.2 on 2022-02-05 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_grades_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='duration',
            field=models.PositiveIntegerField(default=5, verbose_name='duración en años'),
        ),
    ]