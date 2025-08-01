# Generated by Django 5.2.4 on 2025-07-14 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('phone_number', models.CharField(max_length=11, unique=True, verbose_name='Phone number')),
                ('email', models.EmailField(blank=True, max_length=225, null=True, verbose_name='ایمیل')),
                ('first_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Last name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_verified', models.BooleanField(default=False, verbose_name='Verify')),
                ('is_used_free_subs', models.BooleanField(default=False, verbose_name='Is used free subs')),
                ('token', models.CharField(blank=True, editable=False, max_length=64, null=True, verbose_name='Secret token')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update time')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
