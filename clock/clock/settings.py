"""
Django settings for clock project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# Non-secret:
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_EMAIL_SUBJECT_PREFIX = 'Clock-In Registration: '
SEND_ACTIVATION_EMAIL = True
REGISTRATION_AUTO_LOGIN = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
SITE_ID = 1
ADMINS = (('Phil', 'phillipwstewart@gmail.com'))

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'registration',
    'clocks',
    'account'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'clock.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'extras.context_processors.is_mobile',
            ],
        },
    },
]

WSGI_APPLICATION = 'clock.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        #'ATOMIC_REQUESTS' : True,
    }
}

# Load secret info:
SECRET_KEY = ''
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST_PASSWORD = ''
with open('secrets.json', 'r') as f:
    secrets = json.loads(f.read())
    SECRET_KEY = secrets['SECRET_KEY']
    EMAIL_HOST = secrets['EMAIL_HOST']
    EMAIL_HOST_USER = secrets['EMAIL_HOST_USER']
    DEFAULT_FROM_EMAIL = secrets['DEFAULT_FROM_EMAIL']
    SERVER_EMAIL = secrets['DEFAULT_FROM_EMAIL']
    EMAIL_HOST_PASSWORD = secrets['EMAIL_HOST_PASSWORD']
    d = DATABASES['default']
    d['NAME'] = secrets['DATABASE_NAME']
    d['HOST'] = secrets['DATABASE_HOST']
    d['PORT'] = secrets['DATABASE_PORT']
    d['USER'] = secrets['DATABASE_USER']
    d['PASSWORD'] = secrets['DATABASE_PASSWORD']

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = ()
if DEBUG:
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static_debug'),)


