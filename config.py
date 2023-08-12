import os
from pathlib import Path

basedir = Path(__file__).parent.parent
BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"

# class BaseConfig:
UPLOAD_FOLDER = 'C:\projects\myproject\pybo\static\images'
