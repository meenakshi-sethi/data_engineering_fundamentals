import psycopg

# Database connection parameters
conn_params = {
    'host': 'localhost',
    'port': 5487,
    'dbname': 'testdb',
    'user': 'postgres',
    'password': 'postgres'
}

try:
    # Connect to the database
    conn = psycopg.connect(**conn_params)
    cursor = conn.cursor()
    
    # Read 1 record from the names table
    cursor.execute("SELECT firstname, lastname FROM names LIMIT 1")
    record = cursor.fetchone()
    
    if record:
        print(f"First Name: {record[0]}")
        print(f"Last Name: {record[1]}")
    else:
        print("No records found")

    # Insert 2 new records 
    cursor.execute("INSERT INTO names (firstname, lastname) VALUES (%s, %s)", ('John', 'Doe'))
    cursor.execute("INSERT INTO names (firstname, lastname) VALUES (%s, %s)", ('Jane', 'Smith'))
    conn.commit()
    print("\nInserted 2 new records")

    # Read all records
    cursor.execute("SELECT * FROM names")
    all_records = cursor.fetchall()
    print(f"\nAll records ({len(all_records)} total):")
    for record in all_records:
        print(f"  - {record[0]} {record[1]}")


    # Close the connection
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Error: {e}")
