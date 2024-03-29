# Generated by Django 5.0 on 2024-02-15 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CategoryApp', '0001_initial'),
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='project_photos/')),
                ('categories', models.ManyToManyField(to='CategoryApp.category')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.userprofile')),
            ],
        ),
    ]
