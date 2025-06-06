import sqlite3
from lib.db.connection import get_connection

# Run schema.sql to create tables
with open('code-challenge/lib/db/schema.sql', 'r') as f:
    schema_sql = f.read()

conn = get_connection()
conn.executescript(schema_sql)
conn.commit()
conn.close()

# Optionally seed the database
if __name__ == "__main__":
    from lib.db.seed import seed
    seed()
    print("Database setup and seeded.")
