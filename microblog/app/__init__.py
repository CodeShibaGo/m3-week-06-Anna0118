from flask import Flask
from config import Config
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# 載入 .env 檔案
load_dotenv()

# 使用 os.getenv 讀取環境變量
# secret_key = os.getenv('SECRET_KEY')

app = Flask(__name__)
# 防止CSRF攻擊
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'

# 導入資料庫
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models

