import sqlite3
from SQLite3.create_connection import create_connection

# выборка всех категорий
def select_all_categories():
    database = 'render-state.db'
    connection = create_connection(database)
    connection.row_factory = sqlite3.Row # returns a list of dictionaries!
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM categories")
        rows = cursor.fetchall()
    return rows

#выборка категорий по id
def select_category_by_id(id):
    database = 'render-state.db'
    connection = create_connection(database)
    connection.row_factory = sqlite3.Row
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM categories WHERE id=?", (id,))
        row = cursor.fetchone()
    return row

#выборка категорий по item_id
def select_category_by_item_id(item_id):
    database = 'render-state.db'
    connection = create_connection(database)
    connection.row_factory = sqlite3.Row
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM categories WHERE item_id=?", (item_id,))
        row = cursor.fetchone()
    return row

#выборка категорий по category_name
def select_category_by_category_name(category_name):
    database = 'render-state.db'
    connection = create_connection(database)
    connection.row_factory = sqlite3.Row
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM categories WHERE category_name LIKE ?", ('%'+category_name+'%',))
        rows = cursor.fetchall()
    return rows
