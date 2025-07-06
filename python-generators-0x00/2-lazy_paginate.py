import mysql.connector

def paginate_users(page_size, offset):
    """
    Fetches a page of users from the database starting at the given offset.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="your_mysql_user",
            password="your_mysql_password",
            database="ALX_prodev"
        )
        cursor = connection.cursor()
        query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()


def lazy_paginate(page_size):
    """
    Generator that lazily yields pages of users using pagination.
    Only one loop is allowed.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
