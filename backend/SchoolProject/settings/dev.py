from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Dev database (SQLite = simple & fast)
# PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "schooldb",
        "USER": "schooluser",
        "PASSWORD": "schoolpass",
        "HOST": "db",       # matches docker-compose service name
        "PORT": 5432,
    }
}

CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/0"

# Dev-only apps
INSTALLED_APPS += [
    # 'debug_toolbar',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
