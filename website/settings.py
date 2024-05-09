"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 5.0.4.

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
SECRET_KEY = 'django-insecure-c=$ri!b!gw-2ce3+bgxk7-(41)4nl40-de&$53+_t%=f6a93e2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app', 'localhost', 'django-website-qkbcqxh0v-omars-projects-d249164c.vercel.app', 'cloud-clicker-react-app.vercel.app']


# Application definition
# 'webpack_loader',

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapp',
    'rest_framework',
    'corsheaders',
]

# 'django.middleware.csrf.CsrfViewMiddleware',

# 'corsheaders.middleware.CorsMiddleware',
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# CORS_ORIGIN_WHITELIST = [  # Replace with your frontend's domain
#     'http://localhost:3000', 
#     'https://django-website-qkbcqxh0v-omars-projects-d249164c.vercel.app',
#     'https://cloud-clicker-react-app.vercel.app/'
#     # ... add more domains in production if needed
# ]

ROOT_URLCONF = 'website.urls'
# str(BASE_DIR.joinpath('templates'))

# 'django.template.context_processors.csrf',
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'frontend/build')
        ],
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

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',  # Replace with the name you set on RDS
        'USER': 'masteromar',  # Replace with RDS master username 
        'PASSWORD': 'password1',  # Replace with RDS master password
        'HOST': 'clickcounterdb.cjc682sa26n0.us-east-1.rds.amazonaws.com',  # Find this in your RDS instance details
        'PORT': '5432', 
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

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CSRF_USE_SESSIONS = True

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'frontend/build/static'),
)
# 'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
# WEBPACK_LOADER = {
#     'DEFAULT': {
#         'BUNDLE_DIR_NAME': 'webpack_bundles/',
#         'CACHE': not DEBUG,
#         'STATS_FILE': str(BASE_DIR.joinpath('frontend', 'webpack-stats.json')),
#         'POLL_INTERVAL': 0.1,
#         'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
#     }
# }