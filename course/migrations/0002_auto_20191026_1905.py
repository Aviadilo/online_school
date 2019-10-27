# Generated by Django 2.2.6 on 2019-10-26 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_courses', to=settings.AUTH_USER_MODEL, verbose_name='Course owner'),
        ),
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, related_name='student_courses', to=settings.AUTH_USER_MODEL, verbose_name='Students'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(blank=True, null=True, related_name='teacher_courses', to=settings.AUTH_USER_MODEL, verbose_name='Teachers'),
        ),
    ]
