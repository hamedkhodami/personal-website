# Generated by Django 5.2.4 on 2025-07-19 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update Time')),
                ('bio', models.TextField(verbose_name='Biography')),
                ('resume_file', models.FileField(upload_to='resumes/', verbose_name='Resume (PDF)')),
                ('github', models.URLField(blank=True, null=True, verbose_name='GitHub')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='LinkedIn')),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='Telegram')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'About Me',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update Time')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description')),
                ('short_description', models.CharField(max_length=250, verbose_name='Shot Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/image', verbose_name='Image')),
                ('project_url', models.URLField(blank=True, null=True, verbose_name='Live URL')),
                ('github_url', models.URLField(blank=True, null=True, verbose_name='GitHub URL')),
                ('creation_at', models.CharField(blank=True, null=True, verbose_name='Creation At')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update Time')),
                ('title', models.CharField(max_length=64, verbose_name='Skill')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='skill/icon', verbose_name='Icon')),
                ('level', models.CharField(blank=True, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('expert', 'Expert')], default='beginner', null=True, verbose_name='Level')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update Time')),
                ('image', models.ImageField(upload_to='projects/gallery/', verbose_name='Image')),
                ('alt_text', models.CharField(blank=True, max_length=128, verbose_name='Alt Text')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='public.project')),
            ],
            options={
                'verbose_name': 'Project Image',
                'verbose_name_plural': 'Project Images',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='tech_stack',
            field=models.ManyToManyField(blank=True, to='public.skill', verbose_name='Technologies Used'),
        ),
    ]
