# Generated by Django 3.2.16 on 2023-02-17 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_private',
        ),
    ]
