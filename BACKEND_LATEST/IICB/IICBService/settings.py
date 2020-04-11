"""
Django settings for IICBService project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import configparser,os


#*************************************************Replace the lines below***************************************************************

config = configparser.ConfigParser()
config_ini_path=str(os.path.realpath('.')).split('/BACKEND_LATEST')[0]
CONFIGURATION=os.path.join(config_ini_path,'configuration.ini')

#**************************************************Replaced the lines below******************************************************************





config.read(CONFIGURATION)

MEDIA_PATH=config.get('folders','media')
if not os.path.exists(MEDIA_PATH):
    os.makedirs(MEDIA_PATH)
STORAGE_PATH=config.get('folders','IICB_Graph')
if not os.path.exists(STORAGE_PATH):
    os.makedirs(STORAGE_PATH)
CODON_PATH=config.get('folders','CODON_PATH')
if not os.path.exists(CODON_PATH):
    os.makedirs(CODON_PATH)
EXE_PATH=config.get('folders','EXE_PATH')
if not os.path.exists(EXE_PATH):
    os.makedirs(EXE_PATH)
SCI_OUT_PATH=config.get('folders','SCI_OUT_PATH')
if not os.path.exists(SCI_OUT_PATH):
    os.makedirs(SCI_OUT_PATH)
ABOUT_US_PATH=config.get('folders','ABOUT_US_PATH')

if not os.path.exists(ABOUT_US_PATH):
    os.makedirs(ABOUT_US_PATH)
DOWNLOAD_PATH=config.get('folders','DOWNLOAD_PATH')
if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)
GFF_PATH=config.get('folders','GFF_PATH')
if not os.path.exists(GFF_PATH):
    os.makedirs(GFF_PATH)
HELP_PATH=config.get('folders','HELP_PATH')
if not os.path.exists(HELP_PATH):
    os.makedirs(HELP_PATH)



#import os,logging,logging.config
import subprocess,os

subprocess.call(['clear'])










BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY KEY for JayJit
SECRET_KEY = '@n@h)$!0bfm(*$p3no_xgc_ogdi7=d9&7+zgqakj1!0l1%2vk-'
# SECURITY KEY for Utpal
#SECRET_KEY = '#uq^0nb(@diefqtrula&#c8#43864)nx0)=aa2i(#@#69*lb11'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']#'192.168.1.11', '192.168.1.11:4200','localhost','192.168.1.15','KERALA']

CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'rest_framework_swagger',
    'benchmark_django_rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'IICBsrvc'
]

REST_FRAMEWORK = {
    # Parser classes priority-wise for Swagger
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'IICBService.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'IICBService.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


MARIA_HOST=config.get('database','MARIA_HOST')
MARIA_PORT=config.get('database','MARIA_PORT')
MARIA_USER=config.get('database','MARIA_USER')
MARIA_PASSWORD=config.get('database','MARIA_PASSWORD')
MARIA_DB_IICB=config.get('database','MARIA_DB_IICB')
MARIA_DB_SCHEMA_SRES=config.get('database','MARIA_DB_SCHEMA_SRES')
MARIA_DB_SCHEMA_DOTS=config.get('database','MARIA_DB_SCHEMA_DOTS')
MARIA_DB_SCHEMA_CORE=config.get('database','MARIA_DB_SCHEMA_CORE')


DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MARIA_DB_SCHEMA_SRES,
        'USER': MARIA_USER,
        'PASSWORD': MARIA_PASSWORD,
        'HOST': MARIA_HOST,
        'PORT': MARIA_PORT
    }
}





# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_DIR=config.get('folders','media')
#MEDIA_DIR=os.path.join(BASE_DIR,'IICBsrvc/media')
MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(MEDIA_DIR, 'GFF')



import logging,sys
import logging.config

logging.config.fileConfig(CONFIGURATION, disable_existing_loggers=False)

loggers=config.get('loggers','keys')
#print(loggers.split(','))

logger_name=config.get('loggers','logger_name')
logger=logging.getLogger(logger_name)

LOGGER=logger
print=LOGGER.info # once in each module

print("Logging is configured in settings.")

