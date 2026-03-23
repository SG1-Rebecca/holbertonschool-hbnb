import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    if not SECRET_KEY:
        raise ValueError('SECRET_KEY not set')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}