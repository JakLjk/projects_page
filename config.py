import os
from dotenv import load_dotenv

load_dotenv()

ENV_USE_DEV_SETTINGS = bool(int(os.getenv("USE_DEV_SETTINGS", 0)))

ENV_DJ_DB_NAME = os.getenv("DJANGO_DB_NAME")
ENV_DJ_DB_USER = os.getenv("DJANGO_DB_USER")
ENV_DJ_DB_PASSWORD = os.getenv("DJANGO_DB_PASSWORD")
ENV_DJ_DB_HOST = os.getenv("DJANGO_DB_HOST")
ENV_DJ_DB_PORT = os.getenv("DJANGO_DB_PORT")