"""
Django settings for gettingstarted project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
DEFAULT_SECRET_KEY = '3iy-!-d$!pc_ll$#$elg&cpr@*tfn-d5&n9ag=)%#()t$$5%5^'
SECRET_KEY = os.environ.get('SECRET_KEY', DEFAULT_SECRET_KEY)

# Google Drive Storage Security Info
GOOGLE_DRIVE_STORAGE_KEY = """MIICXgIBAAKBgQDYDjYx7xctYy7lXLOPBsd28LhqlCAkLbnsrUIvIi3/EHzLIhnY
32y4PIlIPg1dagVECRL8sYgonWJMBaIxxO8UwqqZ4MDDD21ca9gNXjfZKEnSQdME
qa/kpfX72MwiV7hPwrx2D49CasOE3kp4oSOf8n01CyM7KelCnt0NKNyrYwIDAQAB
AoGBAJcsWn9V68G2RHn4AytwcuCmTmNEgbjOxej00fpo0AZIYwk/MxasPkYrFWOX
B4L1S/nu33owPjUs6jqHNpXcVevHW1Vow8uZTJ7RZ5S1r5t+jk3D87oA8jeSrlcf
VSJP7wqozdjo9riCk7oMsf4nBKrAYbMcQH5v9vpYFPQRb5IBAkEA9bYQWwtaZt2A
2M0Z0MViVm44GtIISv7MMWp6eeL3Gd1/z2hvaDzIlqwr0kz/1EvVPenpj0c4XKQL
OTn9iCGWaQJBAOEaP+Wt+HwfWsgQokik7NNpMyZ1pzgJNbnTn6oNbMbHjHe/NEJ6
fAJ4jNoUoqR0Ag644WEhtm2TOivZTTmhsesCQQDmicZaxhIyBY4I3JdmLGyRz6RQ
ddRWGS8ZBmCXz/4shIiQ39n3oWBLDounK5u1YtlW2AvN5PLa6Qemz+QzP+BRAkBk
4bm/On+BSSALR4EjY16LxLrawqGleGMum8wTjx6v22B1jihinrgS92nQlqzpXOBL
Lso7GLvEUdYhLqrwaCnvAkEAkV3lGEVcbpXZvTc2GoxdNUHSRETt6cP0Slvjx+2o
x7gFYX8nO8Vm0K05A21D2kjLUi5MJqW6uQ5qE4LarsycUg=="""
GOOGLE_DRIVE_STORAGE_SERVICE_EMAIL = '772573684949-bapbrokki21qdaa9do7gqslmt760r0qc@developer.gserviceaccount.com'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gdstorage',
    'hello',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gettingstarted.urls'

WSGI_APPLICATION = 'gettingstarted.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
