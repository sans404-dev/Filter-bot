import sqlite3
from config import db_path


def create_db():
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(
            """create table if not exists users (user_id int, name text, surname text, username text, word text, date text)"""
        )


def store_info(user_id, name, surname, username, word, date):
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO `users` (`user_id`, `name`, `surname`, `username`, `word`, `date`) VALUES(?, ?, ?, ?, ?, ?)",
            (user_id, name, surname, username, word, date),
        )
