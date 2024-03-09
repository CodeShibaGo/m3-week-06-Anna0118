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

## Q: 比較透過ORM和raw SQL的優缺點
 -  ORＭ 適合於快速開發和需要跨資料庫兼容性的項目，因為它提供了一個高層次的抽象來管理資料庫交互
     - 優點: 易維護, 減少SQL injection, 資料庫抽象
     - 缺點：對於較複雜查詢性能度低, 需熟悉抽象概念
 -  raw SQL 提供最大的靈活性和性能優化的可能性，適合於需要進行細粒度控制和優化的場景
     - 優點：易維護, 減少SQL injection, 
     - 缺點: 可維護性差, 增加減少SQL injection,  依賴特定資料庫

## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129
  - 將密碼轉換成另一個格式。基於安全性的理由，要透過某種方式將密碼加密後才存入資料庫中。一般會使用Hash function（雜湊函數，又稱雜湊演算法）來處理這種問題。
  - 由雜湊演算法所計算出來的雜湊值（Hash Value）具有不可逆的性質，也就是說無法逆向演算回原本的數值，因此可有效的保護密碼。 
    - 可以使用 Werkzeug 進行密碼雜湊，也可使用Bcrypt。這兩種Hash 函式庫都可以在Flask中選用。 
    - `generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)` 函數用於產生密碼的散列值。它接受用戶的明文密碼作為輸入，然後使用指定的散列算法（預設為 pbkdf2:sha256）和鹽值長度（預設為8位）來產生一個密碼的散列值（Hash）。
    - `check_password_hash(hash, password)` 函數用於驗證明文密碼與散列值是否匹配。它接受兩個參數：存儲的密碼散列值和用戶輸入的明文密碼。
  - 藉由 generate_password_hash 提供了一種安全的方法來存儲用戶密碼的散列值，而 check_password_hash 則用於驗證用戶登錄時提供的密碼是否正確。這種方法提高了應用程序的安全性，防止密碼洩露的風險。