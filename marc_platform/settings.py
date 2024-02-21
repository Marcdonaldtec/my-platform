"""
Django settings for marc_platform project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9)%zg00o*(7+%kakp-u!c7kb0bgnn*3m-qw!g&u3q0e+*4eu$)'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['.onrender.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'UserApp',
    'AuthenticationApp',
    'CategoryApp',
    'MainApp',
    'ProjectApp',
    'whitenoise',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    
]

ROOT_URLCONF = 'marc_platform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'marc_platform.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / "static"]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR / "media")


AWS_ACCESS_KEY_ID = 'AKIATPRQOVAGVNTCOI64'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'mybucketawsformediafiles'
AWS_S3_REGION_NAME = 'us-east-2'  # par exemple, 'us-east-1'

# Configurations supplémentaires
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',  # Cache pendant 24 heures
}

# Stockage statique (CSS, JavaScript, etc.)
AWS_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Stockage des fichiers médias (images, vidéos, etc.)
AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_PUBLIC_MEDIA_LOCATION}/'



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if DEBUG:
    INTERNAL_IPS = [
        '127.0.0.1',

    ]

    
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}


if DEBUG:
    # Utilisez le stockage local pour les fichiers statiques et médias en développement
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    STATICFILES_DIRS = [BASE_DIR / "static"]
    MEDIA_ROOT = BASE_DIR / "media"
