# Generated by Django 4.2.10 on 2024-02-18 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.courses'),
        ),
    ]