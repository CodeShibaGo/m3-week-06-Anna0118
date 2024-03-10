# scripts/test_script.py
# 用來測試資料庫

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

# 確保在應用上下文中執行db操作
with app.app_context():
    # 使用 SQLAlchemy 的 text 來做原生 raw SQL 查询
    sql = text('SELECT * FROM post')
    result = db.session.execute(sql)
    names = [row for row in result]
    print(names)