from flask import Flask
from config import Config
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler

# 載入 .env 檔案
load_dotenv()

app = Flask(__name__)
app.debug = False
# 防止CSRF攻擊
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'

# 導入資料庫
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

mail_handler = SMTPHandler(
    mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
    fromaddr='no-reply@' + app.config['MAIL_SERVER'],
    toaddrs=app.config['ADMINS'], subject='System-error')

mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
))

if not app.debug:
    app.logger.addHandler(mail_handler)

from app import routes, models, errors

