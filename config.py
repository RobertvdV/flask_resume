import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # WEBSITE PROTECTION
    SECRET_KEY = os.environ.get('SECRET_KEY')
