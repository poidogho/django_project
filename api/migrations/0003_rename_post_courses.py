# Generated by Django 4.2.10 on 2024-02-16 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Courses',
        ),
    ]