import logging
import os

from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask
from flask_bootstrap import Bootstrap5
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap5(app)

# Blueprint Registration
from app.main import bp as main_bp
from app.errors import bp as errors_bp

app.register_blueprint(main_bp)
app.register_blueprint(errors_bp)


if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/website.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Website startup')
