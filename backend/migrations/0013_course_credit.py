# Generated by Django 4.0.2 on 2022-02-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_remove_program_duration_course_weeks'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credit',
            field=models.IntegerField(default=0, verbose_name='creditos del curso'),
        ),
    ]
