"""
Django settings for app project, on Heroku. For more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
import dj_database_url
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: change this before deploying to production!
SECRET_KEY = 'i+acxn5(akgsn!sr4^qgf(^m&*@+g1@u^t@=8s@axc41ml*f=s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', '1') == '1'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_jwt',
    'djangorestframework_camel_case',
    'dynamic_rest',
    'storages',
    'corsheaders',
    # 'crispy_forms',
    'rucken_todo'
)

AUTH_USER_MODEL = 'rucken_todo.User'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'app.helpers.disable_csrf.DisableCSRF'
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Parse database configuration from $DATABASE_URL
if os.environ.get('DATABASE_URL', None) is not None:
    DATABASES['default'] = dj_database_url.config(default=os.environ.get('DATABASE_URL'))

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',  # Any other renders
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',  # Any other parsers
    )
}

DYNAMIC_REST = {
    # DEBUG: enable/disable internal debugging
    'DEBUG': DEBUG,

    # ENABLE_BROWSABLE_API: enable/disable the browsable API.
    # It can be useful to disable it in production.
    'ENABLE_BROWSABLE_API': True,

    # ENABLE_LINKS: enable/disable relationship links
    'ENABLE_LINKS': False,

    # ENABLE_SERIALIZER_CACHE: enable/disable caching of related serializers
    'ENABLE_SERIALIZER_CACHE': True,

    # ENABLE_SERIALIZER_OPTIMIZATIONS: enable/disable representation speedups
    'ENABLE_SERIALIZER_OPTIMIZATIONS': True,

    # DEFER_MANY_RELATIONS: automatically defer many-relations, unless
    # `deferred=False` is explicitly set on the field.
    'DEFER_MANY_RELATIONS': False,

    # MAX_PAGE_SIZE: global setting for max page size.
    # Can be overriden at the viewset level.
    'MAX_PAGE_SIZE': 100,

    # PAGE_QUERY_PARAM: global setting for the pagination query parameter.
    # Can be overriden at the viewset level.
    'PAGE_QUERY_PARAM': 'cur_page',

    # PAGE_SIZE: global setting for page size.
    # Can be overriden at the viewset level.
    'PAGE_SIZE': None,

    # PAGE_SIZE_QUERY_PARAM: global setting for the page size query parameter.
    # Can be overriden at the viewset level.
    'PAGE_SIZE_QUERY_PARAM': 'per_page',

    # ADDITIONAL_PRIMARY_RESOURCE_PREFIX: String to prefix additional
    # instances of the primary resource when sideloading.
    'ADDITIONAL_PRIMARY_RESOURCE_PREFIX': '+',

    # Enables host-relative links.  Only compatible with resources registered
    # through the dynamic router.  If a resource doesn't have a canonical
    # path registered, links will default back to being resource-relative urls
    'ENABLE_HOST_RELATIVE_LINKS': True
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'app.helpers.jwt_utils.jwt_response_payload_handler'
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region
AWS_S3_HOST = 's3.eu-central-1.amazonaws.com'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
if DEBUG:
    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
else:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
    AWS_PRELOAD_METADATA = True  # necessary to fix manage.py collectstatic command to only upload changed files instead of all files
    STATIC_URL = 'http://%s.%s/%s/' % (AWS_STORAGE_BUCKET_NAME, AWS_S3_HOST, 'static')
