"""
Django settings for event_forms_backend project.
"""
import os

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
DOMAIN_NAME = os.getenv('DOMAIN_NAME')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    os.getenv('DOMAIN_NAME'),
    os.getenv('REMOTE_HOST'),
    os.getenv('LOCAL_HOST'),
    '127.0.0.1',
    'localhost'
]
WEB_HOOK = os.getenv('BITRIX_WEB_HOOK')
LINK_FIELD = os.getenv('BITRIX_LINK_FIELD')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'forms.apps.FormsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",  # Заменить на порт Vue.js приложения
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ]
}

ROOT_URLCONF = 'event_forms_backend.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'event_forms_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'event_forms_db',  # Имя вашей локальной базы данных
            'USER': 'postgres',  # Имя пользователя PostgreSQL
            'PASSWORD': 'postgres',  # Пароль пользователя PostgreSQL
            'HOST': 'localhost',  # Или IP-адрес вашего сервера PostgreSQL
            'PORT': '5432',  # Стандартный порт PostgreSQL
        }
    }
else:
    # Postgres
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('POSTGRES_USER'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT')
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', default='ru')

TIME_ZONE = os.getenv('TIME_ZONE', default='Europe/Moscow')

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/events/static/'
if DEBUG:
    # статика в режиме разработчика
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/events/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
