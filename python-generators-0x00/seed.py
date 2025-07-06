import mysql.connector
import csv
import uuid

# ---------- DATABASE CONNECTION SETUP ----------

def connect_db():
    """Connects to the MySQL server (not the database yet)."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"
    )

def create_database(connection):
    """Creates ALX_prodev database if it doesn't exist."""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    connection.commit()
    cursor.close()

def connect_to_prodev():
    """Connects directly to ALX_prodev database."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="ALX_prodev"
    )

# ---------- TABLE CREATION & DATA INSERTION ----------

def create_table(connection):
    """Creates the user_data table if it doesn't exist."""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(10) PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX (user_id)
        )
    """)
    connection.commit()
    cursor.close()

def insert_data(connection, data):
    """Inserts data into user_data table if it does not already exist."""
    cursor = connection.cursor()
    for row in data:
        user_id, name, email, age = row
        cursor.execute("SELECT COUNT(*) FROM user_data WHERE user_id = %s", (user_id,))
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                (user_id, name, email, age)
            )
    connection.commit()
    cursor.close()

# ---------- MAIN SCRIPT ----------

def read_csv_data(filename="user_data.csv"):
    """Reads and yields data from the CSV file."""
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            yield row  # row = [user_id, name, email, age]

if __name__ == "__main__":
    # Step 1: Connect to MySQL server and create the database
    server_conn = connect_db()
    create_database(server_conn)
    server_conn.close()

    # Step 2: Connect to ALX_prodev and set up the table
    db_conn = connect_to_prodev()
    create_table(db_conn)

    # Step 3: Insert data from CSV
    sample_data = list(read_csv_data())  # Convert generator to list
    insert_data(db_conn, sample_data)

    db_conn.close()
    print("✅ Database seeded successfully.")
