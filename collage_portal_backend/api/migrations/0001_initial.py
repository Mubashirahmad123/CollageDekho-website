# Generated by Django 5.0.3 on 2024-03-18 08:49

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
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=3, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('flag_image', models.ImageField(blank=True, null=True, upload_to='country_flags/')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=12)),
                ('stream', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('total_avg_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('curriculum', models.TextField(blank=True, null=True)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('career_opportunities', models.TextField(blank=True, null=True)),
                ('research_areas', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Specializations',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=60)),
                ('state', models.CharField(blank=True, max_length=60)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=20, null=True)),
                ('website', models.URLField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('accreditation_status', models.CharField(blank=True, max_length=100, null=True)),
                ('establishment_date', models.DateField(blank=True, null=True)),
                ('institution_type', models.CharField(blank=True, max_length=50, null=True)),
                ('affiliation', models.CharField(blank=True, max_length=100, null=True)),
                ('campus_facilities', models.TextField(blank=True, null=True)),
                ('ranking', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='college_images/')),
                ('virtual_tour_link', models.URLField(blank=True, max_length=100, null=True)),
                ('virtual_360_tour', models.ImageField(blank=True, null=True, upload_to='virtual_tours/')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.country')),
            ],
            options={
                'verbose_name_plural': 'Colleges',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('duration', models.DurationField()),
                ('eligibility', models.TextField(blank=True, null=True)),
                ('total_avg_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.college')),
                ('specialization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.specialization')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('head_of_department', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='department_images/')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.college')),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.IntegerField()),
                ('fee_structure', models.TextField(blank=True, max_length=20, null=True)),
                ('tuition_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tuition_fee_description', models.TextField(blank=True, null=True)),
                ('hostel_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hostel_fee_description', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
            ],
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('requirements', models.TextField(blank=True, null=True)),
                ('entrance_exam', models.CharField(blank=True, max_length=100, null=True)),
                ('exam_date', models.DateField(blank=True, null=True)),
                ('admission_link', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.college')),
                ('fee_structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.fee')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.IntegerField()),
                ('remarks', models.TextField()),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.college')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('preferences', models.JSONField(blank=True, null=True)),
                ('password', models.CharField(max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.form')),
            ],
        ),
    ]
