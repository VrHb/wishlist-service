import os
from pathlib import Path

from environs import Env
import dj_database_url

env = Env()
env.read_env()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env.str('DJANGO_SECRET_KEY')

DEBUG = env.bool('DEBUG', False)

ALLOWED_HOSTS = env.list('HOSTS', ['127.0.0.1', '0.0.0.0'])

INTERNAL_IPS = env.list('INTERNAL_IPS', ['127.0.0.1', '0.0.0.0'])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'social_django',
    
    'wl_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wishlists.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = os.path.join(BASE_DIR, env.str('STATIC_DIR_NAME', 'staticfiles'))

WSGI_APPLICATION = 'wishlists.wsgi.application'

DATABASES = {
    'default': 
        dj_database_url.config(
            default=env('PSQL_URL')
        )
}


AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

SOCIAL_AUTH_DJANGO_POSTGRES_JSONFIELD = True

SOCIAL_AUTH_VK_OAUTH2_KEY = env('VK_OAUTH_SECRET_KEY')
SOCIAL_AUTH_VK_OAUTH_SECRET = env('VK_OAUTH_SERVICE_KEY')

SOCIAL_AUTH_GITHUB_KEY=env('GITHUB_CLIENT_ID')
SOCIAL_AUTH_GITHUB_SECRET=env('GITHUB_CLIENT_SECRET')

SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'wishlists'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'log.log')
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
}

