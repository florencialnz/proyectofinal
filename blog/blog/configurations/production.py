from .base import *

DEBUG = False
SECRET_KEY='ybt--2&svpe3j0hs3a!j4)6^s*a(zeh)$%evbjdd1hz@o_)kfw'
# TODO: Configurar el dominio al hacer deploy a production
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'midominio-production.com']

# TODO: Configurar db para production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

        # En caso de usar una postgres
        # 'ENGINE': 'django.db.backends.postgresql',

        # En caso de usar una mysql
        # 'ENGINE': 'django.db.backends.mysql',

        # 'NAME': os.getenv('DB_NAME'),

        # 'USER': os.getenv('DB_USER'),

        # 'PASSWORD': os.getenv('DB_PASSWORD'),

        # 'HOST': os.getenv('DB_HOST'),

        # 'PORT': os.getenv('DB_PORT'),
    }
}

os.environ['DJANGO_PORT'] = '8080'