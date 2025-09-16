"""Legacy database initialization script.

NOTE: This script is retained for historical/workshop comparison purposes.
The application now relies on SQLAlchemy's ORM (`db.create_all()`) for schema
creation. Prefer running:

    flask --app app shell -c "from app import db; db.create_all()"

or simply starting the app which auto-executes `create_all()` in development.

Using raw SQL here risks schema drift if the ORM model changes.
"""

import sqlite3

DB_PATH = "instance/db.sqlite"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    complete BOOLEAN NOT NULL DEFAULT 0
);
"""

def main():  # pragma: no cover - legacy utility
    print("[DEPRECATED] Prefer using SQLAlchemy's create_all(); this script may be removed.")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE_SQL)
    conn.commit()
    conn.close()
    print("Legacy init complete (schema ensured).")

if __name__ == "__main__":
    main()
