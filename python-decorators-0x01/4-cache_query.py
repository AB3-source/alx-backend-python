import time
import sqlite3 
import functools

# Simple in-memory query cache
query_cache = {}

# ✅ DB connection decorator
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# ✅ Cache query decorator
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query):
        if query in query_cache:
            print("✅ Returning cached result")
            return query_cache[query]
        result = func(conn, query)
        query_cache[query] = result
        print("📌 Caching new result")
        return result
    return wrapper

# ✅ Main function to fetch users with caching
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# ✅ Test the caching behavior
users = fetch_users_with_cache(query="SELECT * FROM users")       # Caches result
users_again = fetch_users_with_cache(query="SELECT * FROM users") # Uses cache
