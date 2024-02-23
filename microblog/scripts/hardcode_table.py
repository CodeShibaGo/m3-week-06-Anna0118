from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv('DATABASE_URL'))

try:
    with engine.begin() as con:
        con.execute(text("DROP TABLE IF EXISTS book"))
        con.execute(text("""
        CREATE TABLE book (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            primary_author VARCHAR(255)
        )"""))

        data = [
            {"title": "The Hobbit", "primary_author": "Tolkien"},
            {"title": "The Silmarillion", "primary_author": "Tolkien"},
            {"title": "The Witcher", "primary_author": "Anna"},
        ]

        for line in data:
            con.execute(text("""INSERT INTO book(title, primary_author) 
                                VALUES(:title, :primary_author)"""), line)
        con.commit()
except SQLAlchemyError as e:
    print(e)

with engine.connect() as con:
    rs = con.execute(text("SELECT * FROM book"))
    for row in rs:
        print(row)

# -------------------------------------------
# Using SQLAlchemy
# from sqlalchemy import create_engine
# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
# from sqlalchemy import inspect
# from sqlalchemy.sql import text
# from sqlalchemy.exc import SQLAlchemyError
#
# import os
# from dotenv import load_dotenv
# load_dotenv()
#
# # print(sqlalchemy.__version__)
#
# # Creating a Table
# metadata = MetaData()
# books = Table('book', metadata,
#   Column('id', Integer, primary_key=True),
#   Column('title', String(255)),
#   Column('primary_author', String(255)),
# )
# ## create a database engine with which we can connect.
# engine = create_engine(os.getenv('DATABASE_URL'))
# ## use the .create_all() method of our metadata object and pass the engine connection to it,
# ## which will automatically cause SQLAlchemy to generate our table
# metadata.create_all(engine)
#
# ## view the columns and verify our table was successfully created
# # inspector = inspect(engine)
# # print(inspector.get_columns('book'))
#
# try:
#     with engine.connect() as con:
#         statement = text("""INSERT IGNORE INTO book(id, title, primary_author) VALUES(:id, :title, :primary_author)""")
#
#         data = ({"id": 1, "title": "The Hobbit", "primary_author": "Tolkien"},
#                 {"id": 2, "title": "The Silmarillion", "primary_author": "Tolkien"},
#                 {"title": "The Witcher", "primary_author": "Anna"},
#                 )
#         for line in data:
#         # 解包為命名參數，傳遞給 con.execute 方法，防止SQL injection
#             con.execute(statement,line)
#         con.commit()
# except SQLAlchemyError as e:
#     print(e)
#
# with engine.connect() as con:
#     statement = text('SELECT * FROM book')
#     rs = con.execute(statement)
#
#     for row in rs:
#         print(row)
