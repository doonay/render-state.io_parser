import sqlite3
from SQLite3.create_connection import create_connection

def create_table(connection, create_table_sql):
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)

def db_init():
    database = 'render-state.db'
    connection = create_connection(database)
    sql_create_categories_table = """CREATE TABLE IF NOT EXISTS categories (
        id integer NOT NULL PRIMARY KEY,
        item_id integer NOT NULL UNIQUE,
        category_name text NOT NULL,
        link text,
        count integer
    );"""
    if connection is not None:
        create_table(connection, sql_create_categories_table)
    else:
        print("Error! cannot create the database connection.")