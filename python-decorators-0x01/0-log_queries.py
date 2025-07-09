import sqlite3
import functools
import time

# ✅ Decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query', 'UNKNOWN QUERY')
        print(f"[LOG] Executing SQL Query: {query}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"[LOG] Query executed in {duration:.4f} seconds")
        return result
    return wrapper

# ✅ Function using the decorator
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# ✅ Run function to fetch and log users
users = fetch_all_users(query="SELECT * FROM users")
print(users)
