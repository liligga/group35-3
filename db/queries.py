import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / "db.sqlite3")
    cursor = db.cursor()


def create_tables():
    cursor.execute(
        """
        DROP TABLE IF EXISTS category
        """
    )
    cursor.execute(
        """
        DROP TABLE IF EXISTS products
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price DECIMAL,
            image TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES category (id)
        )
        """
    )
    db.commit()

def populate_tables():
    cursor.execute(
        """
        INSERT INTO category (name) VALUES
        ('Книги'), ("Комиксы"), ("Сувениры")
        """
    )
    cursor.execute(
        """
        INSERT INTO products (name, price, image, category_id) VALUES
        ('Мастер и Маргарита', 10.99, 'images/book.jpg', 1),
        ('Война и Мир', 19.99, 'images/book.jpg', 1),
        ('Ромео и Джульета', 29.99, 'images/book.jpg', 1)
        """
    )
    db.commit()

def get_products():
    cursor.execute(
        # """
        # SELECT * FROM products LIMIT 1 OFFSET 1
        # """
        """
        SELECT * FROM products ORDER BY price DESC
        """
    )
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
    pprint(get_products())

# PRIMARY KEY первичный ключ
# FOREIGN KEY внешний ключ
# Products
# 1, 'Мастер и Маргарита', 10.99, 'images/book.jpg', 1
# 2, 'Война и Мир', 19.99, 'images/book.jpg', 1
# 3, 'Ромео и Джульета', 29.99, 'images/book.jpg', 1


# Categories
# 1, "Книги", "Книги - это ....", "images/book_category.jpg"
# 2, "Журналы", "Журналы - это ....", "images/journal_category.jpg"