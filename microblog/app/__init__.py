from flask import Flask
from dotenv import load_dotenv
import os

# 載入 .env 檔案
load_dotenv()

# 使用 os.getenv 讀取環境變量
database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')

app = Flask(__name__)

from app import routes

