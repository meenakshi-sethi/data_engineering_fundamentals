import csv
import psycopg

# Step 1: Create Database
conn = psycopg.connect(
    host="localhost",
    port=5487,
    dbname="postgres", # default name
    user="postgres",
    password="postgres",
    autocommit=True #required for CREATE DATABASE
)
cursor = conn.cursor()

try:
    cursor.execute("CREATE DATABASE csvdb")
    print("Database csvdb created")
except Exception as e:
    print("Database already exists")

cursor.close()
conn.close()

# Step 2: Connect to new DB
connection = psycopg.connect(
    host="localhost",
    port=5487,
    dbname="csvdb",
    user="postgres",
    password="postgres"
)

cur = connection.cursor()

# Step 3: Creating table
cur.execute("""
CREATE TABLE IF NOT EXISTS users(
            id_no INTEGER PRIMARY KEY,
            first_name VARCHAR(25),
            last_name VARCHAR(25))
""")
connection.commit()

# Step 4: Read CSV and insert csv data into db
with open("data/user.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cur.execute("INSERT INTO users (id_no, first_name, last_name) VALUES (%s, %s, %s)",
                    (row["id_no"], row["first_name"], row["last_name"])
                    )

connection.commit()

# Step 5: Validating if data is inserted properly
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
print("\nData in users table:")
for row in rows:
    print(row)

# Step 6: Close connection
cur.close()
connection.close()
print("\nCSV data successfully dumped into csvdb.users")