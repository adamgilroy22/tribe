# Generated by Django 3.2.16 on 2023-02-10 18:02

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(blank=True, max_length=30, null=True)),
                ('bio', models.TextField(blank=True, max_length=150, null=True)),
                ('profile_pic', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='profile_pic')),
                ('bg_pic', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='bg_pic')),
                ('is_suspended', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]