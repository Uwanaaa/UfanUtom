from .base import *
from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = False

ALLOWED_HOSTS = ['ufanutom.com', 'www.ufanutom.com','127.0.0.1']

DJANGO_SETTINGS_MODULE = 'ufanutom.settings'


DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),         
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'POOL_MODE': os.getenv('DATABASE_POOL_MODE')
    }
}