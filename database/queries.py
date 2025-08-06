import sqlite3
from database import get_db
from utils import get_date

def add_weight(weight: float):
  try:
    with get_db() as connection:
      connection.execute(
                "INSERT OR REPLACE INTO weights_data (date, weight) VALUES (?, ?)",
                (get_date(), weight))
  except sqlite3.Error as error:
    print(f"Не удалось добавить вес: {error}")