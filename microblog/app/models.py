# from typing import Optional
from datetime import datetime, timezone
# import sqlalchemy as sa # 資料庫函示和類別，例如型態和查詢建構
# import sqlalchemy.orm as so # 使用模型
from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # id: so.Mapped[int] = so.mapped_column(primary_key=True)

    username = db.Column(db.String(64), index=True, unique=True)
    # username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
    #                                             unique=True)

    email = db.Column(db.String(120), index=True, unique=True)
    # email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
    #                                          unique=True)

    password_hash = db.Column(db.String(128))
    # password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    # 一對多關係
    # `author` 屬性是透過 SQLAlchemy 的 ORM 功能，在 Python 代碼層面定義的。
    # 它用於建立 `User` 和 `Post` 之間的邏輯聯繫，並不對應資料庫中的實體欄位。
    # 這一聯繫依靠 `Post` 表中的 `user_id` 外鍵欄位實現。
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # posts: so.Mapped[List["Post"]] = so.relationship("Post", back_populates="author")  # List["Post"] 作為 posts 的類行註解
    # posts: so.WriteOnlyMapped['Post'] = so.relationship(
    #     back_populates='author')

    # 用來初始化Class類別
    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash

    # 使用print() 顯示我們希望Class出現的的資料
    def __repr__(self):
        return f'username {self.username} , email {self.email},password_hash {self.password_hash}'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=lambda: datetime.now(timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return f'body {self.body}'
