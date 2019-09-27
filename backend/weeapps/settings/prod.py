from .base import *  # noqa

DEBUG = False
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECRET_KEY = os.getenv("SECRET_KEY")
