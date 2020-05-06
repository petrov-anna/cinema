import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SEKRET_KEY') or 'YOU-SHALL-NOT-PASS'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'appd.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False