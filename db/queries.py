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
        CREATE TABLE IF NOT EXISTS Questionaire (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            country TEXT
        )
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


def delete_product():
    # cursor.execute(
    #     """
    #     DELETE FROM products WHERE id = 1
    #     """
    # )
    cursor.execute(
        """
        DELETE FROM products WHERE name ILIKE 'мастер и маргарита'
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


# get_product_by_category_id(1)
def get_product_by_category_id(category_id: int):
    cursor.execute(
        """
        SELECT * FROM products WHERE category_id = :cat_id
        """, {"cat_id": category_id}
    )

    return cursor.fetchall()


def get_product_by_category_name(cat_name: str):
    cursor.execute(
        """
        SELECT * FROM products WHERE category_id = 
        (
            SELECT id FROM category WHERE name = :cat_name
        )
        """, {"cat_name": cat_name}
    )
    return cursor.fetchall()


def get_products_with_category():
    cursor.execute(
        """
        SELECT p.name, c.name FROM products AS p JOIN category AS c ON p.category_id = c.id
        """
    )
    return cursor.fetchall()


def save_questionaire(data):
    print(data)
    cursor.execute(
        """
        INSERT INTO Questionaire (name, age, gender, country) VALUES (:name, :age, :gender, :country)
        """, data
    )
    db.commit()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
    # pprint(get_products())
    # pprint(get_product_by_category_id(2))
    # pprint(get_product_by_category_name("Книги"))
    pprint(get_products_with_category())

# PRIMARY KEY первичный ключ
# FOREIGN KEY внешний ключ
# Products
# 1, 'Мастер и Маргарита', 10.99, 'images/book.jpg', 1
# 2, 'Война и Мир', 19.99, 'images/book.jpg', 1
# 3, 'Ромео и Джульета', 29.99, 'images/book.jpg', 1


# Categories
# 1, "Книги", "Книги - это ....", "images/book_category.jpg"
# 2, "Журналы", "Журналы - это ....", "images/journal_category.jpg"