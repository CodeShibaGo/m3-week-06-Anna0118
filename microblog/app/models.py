from typing import Optional
import sqlalchemy as sa # 資料庫函示和類別，例如型態和查詢建構
import sqlalchemy.orm as so # 使用模型
from app import db
class User(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    # username = db.Column(db.String(128))
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    # 用來初始化Class類別
    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash


    # 使用print() 顯示我們希望Class出現的的資料
    def __repr__(self):
        return f'username {self.username} , email {self.email},password_hash {self.password_hash}'