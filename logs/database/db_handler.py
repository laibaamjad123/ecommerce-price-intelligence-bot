import sqlite3
import os
from utils.logger import logger

class DatabaseHandler:
    def __init__(self):
        os.makedirs("data", exist_ok=True)
        self.conn = sqlite3.connect("data/books.db")
        self.cursor = self.conn.cursor()
        self._create_table()
        logger.info("Database connected!")

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                price REAL,
                rating TEXT,
                category TEXT,
                scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def insert_book(self, title, price, rating, category):
        self.cursor.execute("""
            INSERT INTO books (title, price, rating, category)
            VALUES (?, ?, ?, ?)
        """, (title, price, rating, category))
        self.conn.commit()

    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def get_price_stats(self):
        self.cursor.execute("""
            SELECT 
                COUNT(*) as total,
                ROUND(AVG(price), 2) as avg_price,
                MIN(price) as min_price,
                MAX(price) as max_price
            FROM books
        """)
        return self.cursor.fetchone()

    def get_rating_summary(self):
        self.cursor.execute("""
            SELECT rating, COUNT(*) as count
            FROM books
            GROUP BY rating
            ORDER BY count DESC
        """)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
        logger.info("Database closed!")