from .base import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bmxu&vi39=^=a^1zto6u5t(1dr1f5a^47_of!+m%p6ar*w5a^v'
MIRAGE_SECRET_KEY = 'gdhhgi%&HGKJ*F___fdffhdjfhsh===%@ghg'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS=['bradleylivingarchive.dalang.com.au','indigenousengineering.org.au','livingarchive.teachingforchange.edu.au','127.0.0.1','138.80.128.154','localhost']

EMAIL_BACKEND = 'nullmailer.backend.EmailBackend'
WAGTAILADMIN_BASE_URL="http://localhost:8005"

try:
    from .local import *
except ImportError:
    pass
try:
    from .local import *
except ImportError:
    pass
