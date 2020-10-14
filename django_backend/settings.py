# @Author: Matthew Hale <matthale>
# @Date:   2017-10-20T16:26:07-05:00
# @Email:  mlhale@unomaha.edu
# @Filename: settings.py
# @Last modified by:   matthale
# @Last modified time: 2018-09-06T15:22:25-05:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale



"""
Django settings for django_backend project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from .localsettings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
if ENVIRONMENT == 'PROD':
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['174.74.10.238', '192.168.0.28', 'localhost', 'django']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #just api in production...
    'api',
    'rest_framework',
    #'axes',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#ROOT_URLCONF = 'django_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "static/")],
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

#WSGI_APPLICATION = 'django_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# **** Database config stored in localsettings.py ****


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
#if ENVIRONMENT == 'PROD':
#    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#
#REST_FRAMEWORK = {
#    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
#    'PAGE_SIZE': 10
#}
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
]

REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'api.rest_framework_config.CsrfExemptSessionAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ],
}
