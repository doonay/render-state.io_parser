import sqlite3
from SQLite3.create_connection import create_connection

def insert_one_category(category):
    database = 'render-state.db'
    connection = create_connection(database)
    
    sql = ''' INSERT OR IGNORE INTO categories(
        item_id,
        name,
        link,
        count
    )VALUES(?,?,?,?) '''
    
    with connection:
        cursor = connection.cursor()
        cursor.execute(sql, category)
        connection.commit()
    return cursor.rowcount
