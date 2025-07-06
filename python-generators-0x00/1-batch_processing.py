import mysql.connector

def stream_users_in_batches(batch_size):
    """
    Generator that yields user_data rows in batches of size `batch_size`.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="your_mysql_user",
            password="your_mysql_password",
            database="ALX_prodev"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data")

        batch = []
        for row in cursor:
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:
            yield batch

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()


def batch_processing(batch_size):
    """
    Processes each batch and yields users older than 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            # user format: (user_id, name, email, age)
            if user[3] > 25:
                yield user
