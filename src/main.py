import psycopg

connection = psycopg.connect(
    host = 'localhost',
    port = 5432,
    dbname = 'market_data',
    user='postgres',
    password='password'
)

if connection:
    print("Successfully connected to PostgreSQL!")

cursor = connection.cursor()

cursor.execute("SELECT * FROM prices;")
rows = cursor.fetchall()
for row in rows:
    print(row)