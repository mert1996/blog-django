from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


ALLOWED_HOSTS = ["merttekin.com","127.0.0.1","52.207.189.254"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME":env("DB_NAME"),
        "USER":env("DB_USER"),
        "PASSWORD":env("DB_PASSWORD"),
        "HOST":"localhost",
        "PORT":5432
    }
}

sentry_sdk.init(
  dsn=env("SENTRY_DSN"),
  integrations=[DjangoIntegration()],
  traces_sample_rate=1.0,
  send_default_pii=True
)

AWS_ACCESS_KEY_ID=env("ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=env("SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME="django-blog-application"
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS= {
    "CacheControl": "max-age=86400",
}
AWS_LOCATION="static"
STATIC_URL="http://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE="storages.backends.s3boto3.S3Boto3Storage"

DEFAULT_FILE_STORAGE = "config.storage_backends.MediaStorage"