import os

from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get('DB_HOST', 'db')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('POSTGRES_DB', 'postgres')
DB_USER = os.environ.get('POSTGRES_USER', 'postgres')
DB_PASS = os.environ.get('POSTGRES_PASSWORD', 'postgres')

SECRET = os.environ.get('SECRET', 'SECRET')

USE_HUNTER_URL = os.environ.get('USE_HUNTER_URL', 'False')
HUNTER_URL = os.environ.get('HUNTER_URL', None)
HUNTER_IO_API_KEY = os.environ.get('HUNTER_IO_API_KEY', None)
