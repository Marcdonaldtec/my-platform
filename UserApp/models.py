from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, default='') 
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)

    # Additional fields
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    home_city = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    public_email = models.EmailField(blank=True, null=True)
    short_bio = models.TextField(blank=True, null=True)
    personal_website = models.URLField(blank=True, null=True)
    facebook_profile = models.URLField(blank=True, null=True)
    instagram_profile = models.URLField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    github_profile = models.URLField(blank=True, null=True)
    stackoverflow_profile = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username


