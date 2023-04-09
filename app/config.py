from os import environ
from dotenv import load_dotenv

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
NOTES_PER_PAGE = 4

load_dotenv()