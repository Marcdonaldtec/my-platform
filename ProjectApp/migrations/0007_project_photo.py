# Generated by Django 5.0.2 on 2024-02-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0006_remove_project_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='project_photos/'),
        ),
    ]
