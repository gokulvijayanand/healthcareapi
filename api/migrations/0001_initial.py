# Generated by Django 5.0.2 on 2024-03-07 09:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_registered', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('specialization', models.CharField(choices=[('Cardiology', 'Cardiology'), ('Dermatology', 'Dermatology'), ('Orthopedics', 'Orthopedics'), ('Pediatrics', 'Pediatrics'), ('Psychiatry', 'Psychiatry'), ('Surgery', 'Surgery'), ('Neurology', 'Neurology'), ('Gastroenterology', 'Gastroenterology'), ('Oncology', 'Oncology'), ('Obstetrics and Gynecology', 'Obstetrics and Gynecology'), ('Endocrinology', 'Endocrinology'), ('Radiology', 'Radiology'), ('Ophthalmology', 'Ophthalmology'), ('Urology', 'Urology'), ('Otolaryngology', 'Otolaryngology'), ('Infectious Disease', 'Infectious Disease')], max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('office_number', models.CharField(max_length=15)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('qualifications', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.qualification')),
            ],
        ),
    ]