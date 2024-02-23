# Questions

## Q: 使用 `virtualenv` 建立虛擬環境 #116
1. 在Terminal安裝 virtualenv 套件
```commandline
 pip3 install virtualenv
```
2. 創建虛擬環境
```commandline
 virtualenv venv
```
3. 啟動虛擬環境 (for macOS or Linux)
```commandline
source venv/bin/activate
```

## Q: python-dotenv 如何使用？ #119

`python-dotenv` 是一個用於管理和載入 `.env` 檔案中環境變數的 Python 函式庫，將一些重要的資料存在環境變數(environment variable)中．不僅可以避免將中的資料或敏感資訊 (如資料庫密碼、API密鑰等) 被commit到codebase，
也可用於環境變數區隔開發(development)、測試和生產(production)環境。

1.安裝 `python-dotenv`套件

```commandline
 pip install python-dotenv
```
2.創建一個 `.env`檔案，並寫入環境變變數
```
DATABASE_URL=example_database_url
SECRET_KEY=example_secret_key
```
3.新增一個 .gitingnore 將不需要commit的檔案寫入裡面

## Q:.env 跟 .flaskenv 的差別 #119

在 Flask 應用程式中，`.env` 與 `.flaskenv` 檔案用於存儲環境變量，但各有其專用場景：

- `.env` 主要負責敏感及配置資訊的存儲，適合所有 Python 項目。
- `.flaskenv` 專注於 Flask 應用的運行配置，方便開發者管理。
- 兩者結合使用，實現配置與運行環境設定的有效隔離與管理。

## Q: 如何使用 Flask-SQLAlchemy 連接上 MySQL？ #123
- 先安裝套件
  ```python
  pip install flask-sqlalchemy pymysql
  ```
- 在python檔案中匯入套件
  ```python
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    # 更換下面的用户名、密碼、主機和資料庫名稱
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/mydatabase'
    # 代表資料庫的 db 物件
    db = SQLAlchemy(app)

  ```
- 測試資料庫是否連接成功。在終端機出入 `flask shell`，之後依序輸入以下
  ```python
    # 創建新用戶
    new_user = User(username='testuser')
    db.session.add(new_user)
    db.session.commit()
    
    # 查詢用户
    user = User.query.filter_by(username='testuser').first()
    print(user)
  ```

## Q: Flask-Migrate 如何使用？ #124
- 先安裝Flask-Migrate套件
  ```python
  pip install Flask-Migrate
  ```
- 新增資料庫模型， (app/models.py)
  ```python
  from app import db
  # 範例
  class Users(db.Model):    
    _id = db.Column('id', db.Integer, primary_key=True)   
    name = db.Column('name', db.String(100))    
    email = db.Column(db.String(100)) 
   
    def __init__(self, name, email):  
        self.name =name    
        self.email = email
  ```
- 在python檔案中匯入
  ```python
  from flask_migrate import Migrate
  Migrate(app,db)
  ```
- 使用command line 指令執行Flask Migrate
  ```python
  # 會出現一個migrations資料夾
  flask db init
  flask db migrate -m "說明文字"
  # 將migrations檔案更新至資料庫中
  flask db upgrade
  ```
## Q: 如何使用 SQLAlchemy 下 Raw SQL？ #125
  - 在 SQLAlchemy 中，透過```connection.execute()```，例如：connection.execute(text("SELECT * FROM my_table"))
  - 執行後需要再使用 ```connection.commit()``` 來提交資料，確保更改和保存到資料庫中。

## Q: 如何用土炮的方式建立 Table？ #126
  - 在 SQLAlchemy 中，可以直接透過 CREATE TABLE 的 SQL 語句來達成
  - 例如：connection.execute(text("CREATE TABLE table_name (id INTEGER PRIMARY KEY, name VARCHAR(100))"))

## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129