import os
from dotenv import load_dotenv

load_dotenv()

ENV_PROJECT_SLUG = (os.getenv("PROJECT_SLUG", "PROJECT_DEFAULT_SLUG"))

ENV_USE_DEV_SETTINGS = bool(int(os.getenv("USE_DEV_SETTINGS", 0)))
ENV_RUN_IN_DEBUG_MODE = bool(int(os.getenv("RUN_IN_DEBUG_MODE", 0)))

ENV_SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-sbw!p&9l6r7rn(a5m*l!(x1mcal=k$bbre9ey&%3(d8ry^kqix")

ENV_STATIC_FOLDER = os.getenv("STATIC_FOLDER", "/static")

ENV_DJ_DB_NAME = os.getenv("DJANGO_DB_NAME")
ENV_DJ_DB_USER = os.getenv("DJANGO_DB_USER")
ENV_DJ_DB_PASSWORD = os.getenv("DJANGO_DB_PASSWORD")
ENV_DJ_DB_HOST = os.getenv("DJANGO_DB_HOST")
ENV_DJ_DB_PORT = os.getenv("DJANGO_DB_PORT")