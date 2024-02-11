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

## Q: Flask-Migrate 如何使用？ #124

## Q: 如何使用 SQLAlchemy 下 Raw SQL？ #125

## Q: 如何用土炮的方式建立 Table？ #126

## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129