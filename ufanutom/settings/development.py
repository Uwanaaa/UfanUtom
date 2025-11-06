from .base import *
from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = True

ALLOWED_HOSTS = ['*']

DJANGO_SETTINGS_MODULE = 'ufanutom.settings'

INSTALLED_APPS += ['silk']

MIDDLEWARE += ['silk.middleware.SilkyMiddleware']

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', '5432'), 
        'NAME': os.getenv('DATABASE_NAME', 'ufanutom_dev'),
        'USER': os.getenv('DATABASE_USER', 'ufanutom_user'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'ufanutom_password'),
        'POOL_MODE': os.getenv('DATABASE_POOL_MODE', 'default')
    }
}