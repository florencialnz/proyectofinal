from .base import *
DEBUG = False
#TODO CONFIGURAR mi dominio al hacer deploy

ALLOWED_HOSTS = ["midominio-production.com"]
# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #En caso de usar postgres, cambiar a .postgresql, en caso de usar mysql, cambiar a .mysql
        
        #'NAME': os.getenv('DB_NAME'),

        #'USER': os.getenv('DB_USER'),

        #'PASSWORD': os.getenv('DB_PASSWORD'),

        #'HOST': os.getenv('DB_HOST'),

        #'PORT': os.getenv('DB_PORT'),
    }
}

os.environ['DJANGO_PORT'] = "8000"