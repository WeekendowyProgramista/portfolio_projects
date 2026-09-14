import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cursor = connection.cursor(cursor_factory=RealDictCursor)
cursor.execute('SELECT * from child;')
record = cursor.fetchall()

for child in record:
    print(f"ID: {child['child_id']} | First_name: {child['first_name']} | Last_name: {child['last_name']}")

cursor.close()
connection.close()