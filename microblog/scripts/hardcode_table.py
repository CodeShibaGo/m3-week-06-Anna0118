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