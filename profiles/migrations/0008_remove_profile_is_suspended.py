# Generated by Django 3.2.16 on 2023-03-04 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20230228_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_suspended',
        ),
    ]
