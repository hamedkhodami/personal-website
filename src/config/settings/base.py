from pathlib import Path
import os
from dotenv import load_dotenv
# -----------------------------------------------------------------


# ---BASE_DIR------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# -----------------------------------------------------------------


# ---ENV-----------------------------------------------------------
load_dotenv(dotenv_path=BASE_DIR / '.env')
# -----------------------------------------------------------------


# ---SECURITY------------------------------------------------------
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = bool(int(os.getenv('DEBUG', 1)))
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
# -----------------------------------------------------------------


# ---CSRF---------------------------------------------------------
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED', 'http://127.0.0.1',).split(',')
# ----------------------------------------------------------------


# ---Application definition---------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'apps.core.apps.CoreConfig',
    'apps.account.apps.AccountConfig',
    'apps.contactus.apps.ContactusConfig',
    'apps.public.apps.PublicConfig',

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

ROOT_URLCONF = 'config.urls'
# ----------------------------------------------------------------


# ---TEMPLATES----------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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
# ----------------------------------------------------------------


# ---WSGI---------------------------------------------------------
WSGI_APPLICATION = 'config.wsgi.application'
# ----------------------------------------------------------------


# ---WSGI---------------------------------------------------------
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
# ----------------------------------------------------------------


# ---Internationalization------------------------------------------
LANGUAGES = [
    ('fa', "Persian"),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = False
# ----------------------------------------------------------------


# ---Static files-------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.getenv('STATIC_ROOT')

STATICFILES_DIRS = [
   os.getenv('STATICFILES_DIRS', BASE_DIR / 'static/assets/'),
]
# ----------------------------------------------------------------


# ---Media--------------------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / os.getenv('MEDIA_ROOT', 'static/media')
# ----------------------------------------------------------------


# ---Production whitenoise----------------------------------------
if int(os.getenv('ENABLE_WHITENOISE', default=0)):
    # Insert Whitenoise Middleware and set as StaticFileStorage
    MIDDLEWARE += [
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]
    STATICFILES_STORAGE = 'whitenoise.storage.StaticFilesStorage'
# ----------------------------------------------------------------


# ---Default primary key field type------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# ---------------------------------------------------------------


# ---Auth user model---------------------------------------------
AUTH_USER_MODEL = 'account.User'
# ---------------------------------------------------------------


# ---REDIS-------------------------------------------------------
REDIS_CONFIG = {
    'active': int(os.getenv('REDIS_ACTIVE', 0)),  # 1 redis is connected, 0 not connected
    'host': os.getenv('REDIS_HOST', 'localhost'),
    'port': int(os.getenv('REDIS_PORT', 6379))
}
# ---------------------------------------------------------------


# ---EMAIL-------------------------------------------------------
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') == 'True'
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
# ---------------------------------------------------------------


# ---CELERY config------------------------------------------------
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379')
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_DEFAULT_QUEUE = 'default'
# ----------------------------------------------------------------
