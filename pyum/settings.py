import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iq$-8#slq=%nf#r(bas&o$miin+b_(dxy^wfu(uwe-^y28(wh#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'app',
    'django_tables2'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request'
)

ROOT_URLCONF = 'pyum.urls'

WSGI_APPLICATION = 'pyum.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'erik3333',
        'HOST': '54.85.78.54'
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))
STATIC_URL = '/static/'

ABSOLUTE_PATH = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
MEDIA_ROOT = ABSOLUTE_PATH('media/')