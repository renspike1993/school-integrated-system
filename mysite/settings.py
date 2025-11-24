from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key secret in production
SECRET_KEY = 'django-insecure-change-me-in-production'

DEBUG = True

# For development this is okay — in production specify domains
ALLOWED_HOSTS = ['*','192.168.10.116']


# -------------------------------------------------------------------
# Applications
# -------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'apps.core',
    'apps.app1',
    'apps.app2',
    'apps.app3',
]


# -------------------------------------------------------------------
# Middleware
# -------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    

    # 'core.middleware.RouteAccessLogMiddleware',
    "mysite.middleware.request_logging.RequestLoggingMiddleware",
]
import logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "verbose": {
            "format": "[{asctime}] {levelname} {message}",
            "style": "{",
        },
        "request_verbose": {
            "format": "[{asctime}] {levelname} {method} {path} "
                      "User={user} IP={ip} Status={status_code}",
            "style": "{",
        },
    },

    "handlers": {
        "request_file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "requests.log",
            "formatter": "request_verbose",
        },
    },

    "loggers": {
        "django.request": {
            "handlers": ["request_file"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

ROOT_URLCONF = 'mysite.urls'


# -------------------------------------------------------------------
# Templates
# -------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # shared templates folder
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


# -------------------------------------------------------------------
# WSGI
# -------------------------------------------------------------------
WSGI_APPLICATION = 'mysite.wsgi.application'


# -------------------------------------------------------------------
# Database (SQLite default)
# -------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# -------------------------------------------------------------------
# Authentication Redirects
# -------------------------------------------------------------------
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/login/'



# -------------------------------------------------------------------
# Password validation (empty is OK for dev)
# -------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = []


# -------------------------------------------------------------------
# Internationalization
# -------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# -------------------------------------------------------------------
# Static files
# -------------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']   # shared static
STATIC_ROOT = BASE_DIR / 'staticfiles'     # for collectstatic (prod)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -------------------------------------------------------------------
# Default PK field type
# -------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
