import sqlite3
from datetime import datetime

def init_db() -> None:
    try:
        with sqlite3.connect("database/NutriTrack.db") as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            
            # Таблица для данных о весе
            connection.execute("""
                CREATE TABLE IF NOT EXISTS weights_data (
                    date TEXT PRIMARY KEY,
                    weight REAL NOT NULL
                )
            """)
            
            # Здесь можно добавить создание других таблиц
            # connection.execute("CREATE TABLE IF NOT EXISTS ...")
            
    except sqlite3.Error as error:
        raise sqlite3.Error(f"Failed to initialize database: {error}") from error
    # остальные таблицы
def get_db() -> sqlite3.Connection:
    try:
        connection = sqlite3.connect("database/NutriTrack.db")
        return connection
    except sqlite3.Error as error:
        raise sqlite3.Error(f"Database connection failed: {error}") from error

