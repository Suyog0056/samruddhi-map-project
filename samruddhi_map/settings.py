from pathlib import Path
import os
GDAL_LIBRARY_PATH = r"C:\Program Files\GDAL\gdal.dll"
GEOS_LIBRARY_PATH = r"C:\Program Files\GDAL\geos_c.dll"
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Make sure templates/ folder exists or create it
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
ROOT_URLCONF = 'samruddhi_map.urls'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'rest_framework',
    'maps',
'leaflet'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # required
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # required
    'django.contrib.messages.middleware.MessageMiddleware',  # required
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',  # ✅ GeoDjango + PostgreSQL
        'NAME': 'samruddhi_db',
        'USER': 'postgres',
        'PASSWORD': 'Suyog@2001',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

SECRET_KEY = 'django-insecure-94sj*3%_your_custom_generated_secret_key_here'

STATIC_URL = '/static/'

# Optional if you're placing static files manually inside app
import os
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'maps', 'static')
]


