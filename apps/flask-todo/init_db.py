import sqlite3

DB_PATH = "instance/db.sqlite"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    complete BOOLEAN NOT NULL DEFAULT 0
);
"""

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE_SQL)
    conn.commit()
    conn.close()
    print("Database initialized and 'todo' table created (if not exists).")

if __name__ == "__main__":
    main()
