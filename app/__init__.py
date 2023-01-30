import logging
import os

from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask
from flask_bootstrap import Bootstrap5
from config import Config
from flask_assets import Environment, Bundle


app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap5(app)
assets = Environment(app)

# Blueprint Registration
from app.main import bp as main_bp
from app.errors import bp as errors_bp

app.register_blueprint(main_bp)
app.register_blueprint(errors_bp)

# Asset Registration
assets.url = app.static_url_path
scss = Bundle('src/scss/theme.scss', 
                filters='libsass', 
                depends='src/scss/_user-variables.scss',
                output='css/all.css')
assets.register('scss_all', scss) 

