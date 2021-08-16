import os

# Celery settings
CELERY_BROKER_URL = 'amqp://guest:guest@localhost'
ACCEPT_CONTENT = ['json']
RESULT_BACKEND = 'db+sqlite:///results.sqlite'
TASK_SERIALIZER = 'json'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l!t+dmzf97rt9s*yrsux1py_1@odvz1szr&6&m!f@-nxq6k%%p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'debug_toolbar',
    'app_celery', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'main.wsgi.application'


CELERY = {
    'BROKER_URL': os.environ['CELERY_BROKER'],
    'CELERY_IMPORTS': ('worker.tasks', ),
    'CELERY_TASK_SERIALIZER': 'json',
    'CELERY_RESULT_SERIALIZER': 'json',
    'CELERY_ACCEPT_CONTENT': ['json'],
}


DATA_PATH = '/app/data'

# Database
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',    },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        },
    },
    'handlers': {
        # this is what you see in runserver console
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        # this handler logs to file
        'file': {  
            'class': 'logging.FileHandler',
            'filename': os.path.normpath(os.path.join(BASE_DIR, 'logs/django.log')),  
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            # log to console and file handlers
            'handlers': ['console', 'file'],  
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
             'propagate': True,
        },
    },
}

INTERNAL_IPS = [
    '127.0.0.1',
]