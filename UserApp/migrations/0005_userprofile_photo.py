# Generated by Django 5.0.2 on 2024-02-19 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0004_remove_userprofile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default=5.200748907842729e-05, upload_to='user_photos/'),
            preserve_default=False,
        ),
    ]