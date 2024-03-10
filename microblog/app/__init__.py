from flask import Flask
from config import Config
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler # 導入RotatingFileHandler，用於設置日誌文件的輪替

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

# 電子郵件發送錯誤
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

    # Logging to a File 錯誤檔案日誌
    # 檢查是否存在 'logs' 資料夾，如果不存在則建立資料夾
    if not os.path.exists('logs'):
        os.mkdir('logs')
    # 建立 RotatingFileHandler 物件，設置日誌文件的最大大小為 10KB，保留 10 個備份
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    # 設置日誌格式，包括時間、日誌級別、訊息、路徑和行數
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    # 處理ERROR等級
    file_handler.setLevel(logging.DEBUG)
    # 加入到日誌中
    app.logger.addHandler(file_handler)

from app import routes, models, errors

