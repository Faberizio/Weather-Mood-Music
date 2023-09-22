from .base import *
import environ
#from pathlib import Path

#BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()


env.read_env(str(BASE_DIR.joinpath(".env")))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str('DB_NAME'),           
        "USER": env.str('DB_USER'),           
        "PASSWORD": env.str('DB_PWD'), 
        "HOST": env.str('DB_HOST'),
        "PORT": env.int('DB_PORT'),
    }
}
