# 🔁 Python Generator – Stream Rows from SQL Database

This project demonstrates how to:
- Set up a MySQL database and table
- Insert CSV data into the table
- Use Python generators to stream records from the database one by one

---

## 📁 Files

- `seed.py`: Connects to MySQL, creates `ALX_prodev` database, creates a `user_data` table, and populates it with data from a CSV file.
- `user_data.csv`: Sample data file with fields: `user_id`, `name`, `email`, and `age`.

---

## 📌 Database Setup

- Database Name: `ALX_prodev`
- Table: `user_data`
- Fields:
  - `user_id` (UUID, Primary Key)
  - `name` (VARCHAR, Not Null)
  - `email` (VARCHAR, Not Null)
  - `age` (DECIMAL, Not Null)

---

## ⚙️ Script Functions

### `connect_db()`
Connects to MySQL server (without specifying a DB).

### `create_database(connection)`
Creates the database if it doesn't already exist.

### `connect_to_prodev()`
Connects to `ALX_prodev` database.

### `create_table(connection)`
Creates the `user_data` table.

### `insert_data(connection, data)`
Inserts sample data from CSV into the table, avoiding duplicates.

---

## ✅ Usage

1. Update MySQL credentials in `seed.py`.
2. Ensure `user_data.csv` is present in the same directory.
3. Run the script:

```bash
python3 seed.py
