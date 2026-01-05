# CSV to PostgreSQL Database Loader

A Python-based ETL (Extract, Transform, Load) script that demonstrates how to read data from a CSV file and load it into a PostgreSQL database running in a Docker container.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)
- [Learning Outcomes](#learning-outcomes)

## 🎯 Overview

This project demonstrates a fundamental data engineering workflow: extracting data from a CSV file and loading it into a PostgreSQL database. It's designed as a learning tool for understanding:

- Database connection management
- SQL table creation and data insertion
- CSV file processing
- Python database adapters (psycopg3)
- Virtual environment management
- Docker-based database setup

## ✨ Features

- **Automated Database Creation**: Creates PostgreSQL database if it doesn't exist
- **Dynamic Table Creation**: Creates table schema programmatically
- **CSV Processing**: Reads and parses CSV files using Python's csv module
- **Data Validation**: Displays inserted data for verification
- **Error Handling**: Graceful handling of existing database scenarios
- **Clean Resource Management**: Proper connection and cursor cleanup

## 📦 Prerequisites

Before running this project, ensure you have:

### Required Software

- **Python 3.8+** installed on your system.
- **Docker Desktop** installed and running
- **PostgreSQL Docker Container** running
  ```bash
  docker run -d \
    --name pg-container \
    -e POSTGRES_PASSWORD=postgres \
    -p 5487:5432 \
    postgres
  ```

### Required Knowledge

- Basic understanding of Python
- Familiarity with SQL databases
- Basic command-line operations

## 📁 Project Structure

```
csv-to-db/
├── csvtodb.py          # Main Python script for ETL process
├── requirement.txt     # Python package dependencies
├── .gitignore         # Git ignore rules (excludes venv/)
├── data/
│   └── user.csv       # Sample CSV file with user data
├── venv/              # Virtual environment (not tracked in git)
└── README.md          # This documentation file
```

## 🚀 Installation

### Step 1: Clone the Repository

```bash
cd /path/to/data_engineering_fundamentals
```

### Step 2: Navigate to Project Directory

```bash
cd csv-to-db
```

### Step 3: Create Virtual Environment

A virtual environment isolates your project dependencies from the system Python installation.

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` at the beginning of your terminal prompt.

### Step 4: Install Dependencies

```bash
pip install -r requirement.txt
```

This installs:
- **psycopg[binary]**: PostgreSQL database adapter for Python (version 3)
- **pandas**: Data manipulation library (for future enhancements)
- **python-dotenv**: Environment variable management

### Step 5: Verify Installation

```bash
pip list
```

You should see the installed packages listed.

## ⚙️ Configuration

### Database Connection Settings

The script uses the following PostgreSQL connection parameters:

| Parameter | Value | Description |
|-----------|-------|-------------|
| Host | `localhost` | Database server address |
| Port | `5487` | Mapped port from Docker container |
| Default DB | `postgres` | Initial connection database |
| Target DB | `csvdb` | Database to be created |
| User | `postgres` | Database username |
| Password | `postgres` | Database password |

### Customizing Configuration

To modify database credentials, edit the connection parameters in `csvtodb.py`:

```python
conn = psycopg.connect(
    host="localhost",
    port=5487,
    dbname="postgres",
    user="your_username",      # Change this
    password="your_password",  # Change this
    autocommit=True
)
```

**Best Practice**: Store credentials in environment variables using `python-dotenv`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg.connect(
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", 5487)),
    dbname=os.getenv("DB_NAME", "postgres"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
```

## 💻 Usage

### Running the Script

Ensure your virtual environment is activated (you should see `(venv)` in your terminal):

```bash
python csvtodb.py
```

### Expected Output

```
Database csvdb created

Data in users table:
(1, 'Hannah', 'Montana')
(2, 'Nick', 'Jonas')
(3, 'Taylor', 'Swift')
(4, 'Alan', 'Walker')

CSV data successfully dumped into csvdb.users
```

### What Happens When You Run the Script?

1. **Database Creation**: Connects to default `postgres` database and creates `csvdb`
2. **Table Creation**: Creates `users` table with defined schema
3. **CSV Reading**: Opens and reads `data/user.csv` file
4. **Data Insertion**: Inserts each row from CSV into the database
5. **Validation**: Queries and displays all inserted data
6. **Cleanup**: Closes database connections properly

## 🗄️ Database Schema

### Users Table

```sql
CREATE TABLE IF NOT EXISTS users (
    id_no INTEGER PRIMARY KEY,
    first_name VARCHAR(25),
    last_name VARCHAR(25)
);
```

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id_no` | INTEGER | PRIMARY KEY | Unique identifier |
| `first_name` | VARCHAR(25) | - | User's first name |
| `last_name` | VARCHAR(25) | - | User's last name |

### CSV File Format

Your CSV file should follow this structure:

```csv
id_no,first_name,last_name
1,Hannah,Montana
2,Nick,Jonas
3,Taylor,Swift
4,Alan,Walker
```

**Requirements:**
- Header row must match column names exactly
- `id_no` must be unique integers
- Names should not exceed 25 characters

## ✅ Verification

### Method 1: Using Docker Exec (Quick Check)

```bash
docker exec -it pg-container psql -U postgres -d csvdb -c "SELECT * FROM users;"
```

Expected output:
```
 id_no | first_name | last_name 
-------+------------+-----------
     1 | Hannah     | Montana
     2 | Nick       | Jonas
     3 | Taylor     | Swift
     4 | Alan       | Walker
```

### Method 2: Interactive psql Session

```bash
docker exec -it pg-container psql -U postgres -d csvdb
```

Once inside psql:

```sql
-- List all databases
\l

-- List all tables in current database
\dt

-- Describe users table structure
\d users

-- View all data
SELECT * FROM users;

-- Count total records
SELECT COUNT(*) FROM users;

-- Exit psql
\q
```

### Method 3: Using pgAdmin (GUI)

If you have pgAdmin installed:
1. Connect to `localhost:5487`
2. Navigate to: Servers → PostgreSQL → Databases → csvdb → Schemas → public → Tables → users
3. Right-click on `users` → View/Edit Data → All Rows

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue 1: `ModuleNotFoundError: No module named 'psycopg'`

**Cause**: Virtual environment not activated or packages not installed

**Solution**:
```bash
source venv/bin/activate  # Activate venv
pip install -r requirement.txt
```

#### Issue 2: `Connection refused` or `Could not connect to server`

**Cause**: PostgreSQL container not running

**Solution**:
```bash
# Check if container is running
docker ps

# If not running, start it
docker start pg-container

# Or create a new container
docker run -d --name pg-container -e POSTGRES_PASSWORD=postgres -p 5487:5432 postgres
```

#### Issue 3: `Database "csvdb" already exists`

**Cause**: Script has been run before

**Solution**: This is normal behavior. The script will use the existing database.

To start fresh:
```bash
docker exec -it pg-container psql -U postgres -c "DROP DATABASE csvdb;"
python csvtodb.py
```

#### Issue 4: `UNIQUE constraint violation` or `duplicate key value`

**Cause**: Attempting to insert data with existing primary keys

**Solution**: Clear the table before re-running:
```sql
docker exec -it pg-container psql -U postgres -d csvdb -c "TRUNCATE TABLE users;"
```

#### Issue 5: Using Wrong Python Interpreter

**Cause**: Running with system Python instead of venv Python

**Solution**: 
- Don't use `/usr/local/bin/python3` or full paths
- Just use `python` when venv is activated
- Verify with: `which python` (should show path to venv)

### Debugging Tips

1. **Check Python version**:
   ```bash
   python --version
   ```

2. **Verify package installation**:
   ```bash
   pip show psycopg
   ```

3. **Test database connection**:
   ```bash
   docker exec -it pg-container psql -U postgres -c "SELECT version();"
   ```

4. **Check Docker container logs**:
   ```bash
   docker logs pg-container
   ```

## 📚 Best Practices

### 1. Virtual Environment Usage

- **Always activate** venv before running the script
- **Never commit** venv folder to version control
- **Use requirements.txt** to track dependencies

### 2. Database Security

- **Don't hardcode credentials** in production code
- **Use environment variables** for sensitive data
- **Create .env file** (add to .gitignore):
  ```
  DB_HOST=localhost
  DB_PORT=5487
  DB_NAME=csvdb
  DB_USER=postgres
  DB_PASSWORD=your_secure_password
  ```

### 3. Error Handling

Add comprehensive error handling:
```python
try:
    cursor.execute("CREATE DATABASE csvdb")
    print("Database csvdb created")
except psycopg.errors.DuplicateDatabase:
    print("Database already exists")
except Exception as e:
    print(f"Error creating database: {e}")
```

### 4. Connection Management

Always use context managers or ensure proper cleanup:
```python
try:
    conn = psycopg.connect(...)
    # Do work
finally:
    conn.close()
```

### 5. Data Validation

- Validate CSV data before insertion
- Check for required fields
- Handle data type mismatches

## 🎓 Learning Outcomes

By completing this project, you will learn:

### Python Skills
- ✅ Creating and managing virtual environments
- ✅ Working with CSV files using the `csv` module
- ✅ Database connectivity with psycopg3
- ✅ Error handling and exception management
- ✅ Resource cleanup (connections, cursors)

### SQL & Database Skills
- ✅ Creating databases programmatically
- ✅ Defining table schemas with constraints
- ✅ Executing INSERT, SELECT queries
- ✅ Understanding primary keys
- ✅ Transaction management (commit/rollback)

### DevOps & Tools
- ✅ Using Docker for database management
- ✅ Docker exec commands for container interaction
- ✅ psql command-line tool usage
- ✅ Git version control best practices

### Data Engineering Concepts
- ✅ ETL pipeline basics (Extract, Transform, Load)
- ✅ Data migration workflows
- ✅ Connection pooling concepts
- ✅ Batch data processing

## 🔄 Next Steps

To extend this project, consider:

1. **Add Data Transformation**: Clean and transform CSV data before insertion
2. **Implement Logging**: Add proper logging instead of print statements
3. **Bulk Insert**: Use `executemany()` for better performance
4. **Error Recovery**: Implement rollback on errors
5. **Multiple Files**: Process multiple CSV files
6. **Data Validation**: Add schema validation for CSV files
7. **Incremental Loads**: Track and load only new/changed records
8. **Unit Tests**: Write tests for database operations

## 📝 License

This project is created for educational purposes as part of the Data Engineering Fundamentals series.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements!

## 📧 Contact

For questions or suggestions, please open an issue in the repository.

---

**Happy Learning! 🚀**
- Host: `localhost`
- Port: `5487`
- Database: `csvdb` (created automatically)
- User: `postgres`
- Password: `postgres`

## CSV File Format

The CSV file should have the following columns:
- `id_no` (integer)
- `first_name` (varchar)
- `last_name` (varchar)

Example:
```csv
id_no,first_name,last_name
1,Hannah,Montana
2,Nick,Jonas
```

## Dependencies

- `psycopg[binary]` - PostgreSQL adapter
- `pandas` - Data manipulation library
- `python-dotenv` - Environment variable management

## Notes

- The script creates a database named `csvdb` if it doesn't exist
- If the database already exists, it will use the existing one
- The `users` table is created with `CREATE TABLE IF NOT EXISTS`
- Virtual environment (`venv/`) is excluded from version control
