import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("activity.db")
        self.create_user_table()

    def create_user_table(self):
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
                """
            )

    def add_user(self, username, hashed_password):
        try:
            with self.conn:
                self.conn.execute(
                    "INSERT INTO users (username, password) VALUES (?, ?)",
                    (username, hashed_password),
                )
            return True
        except sqlite3.IntegrityError:
            return False
