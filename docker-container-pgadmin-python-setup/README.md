# Docker PostgreSQL with Python - Complete Guide

A comprehensive guide to setting up Docker Desktop on macOS (M1/M2/M3), installing PostgreSQL in a Docker container, and connecting to it using Python with psycopg.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)
- [What I Learned](#what-i-learned)

---

## 🎯 Project Overview

This project documents my complete journey of:
1. ✅ Installing Docker Desktop on macOS M1
2. ✅ Setting up PostgreSQL in a Docker container
3. ✅ Troubleshooting pgAdmin connection issues
4. ✅ Resolving port mapping conflicts
5. ✅ Creating database tables via CLI
6. ✅ Connecting PostgreSQL to Python using psycopg3
7. ✅ Building a complete example with Jupyter Notebook

> **📌 Note:** This is an educational project for learning Docker, PostgreSQL, and Python integration. All credentials are for local development only.

---

## 📦 Prerequisites

- **macOS** (M1/M2/M3 or Intel)
- **Docker Desktop** (see installation guide)
- **Python 3.8+** (Python 3.13 recommended)
- **Terminal** access

---

## 🚀 Installation Guide

### Step 1: Install Docker Desktop

Follow the detailed guide: **[Docker Installation Guide for macOS](DOCKER_INSTALLATION_GUIDE.md)**

Quick summary:
1. Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop/)
2. Install and run Docker
3. Verify: `docker --version`

### Step 2: Set Up PostgreSQL with Docker

Follow the detailed guide: **[PostgreSQL Setup Guide](POSTGRES_SETUP.md)**

Quick command:
```bash
docker run --name pg-container \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=testdb \
  -p 5487:5432 \
  -d postgres
```

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚡ Quick Start

### Option 1: Using Python Script

```bash
python read_data.py
```

### Option 2: Using Jupyter Notebook

Open `read.ipynb` and run all cells.

### Option 3: Using Docker CLI

Start PostgreSQL container:
```bash
docker run --name pg-container \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=testdb \
  -p 5487:5432 \
  -d postgres
```

Run the Python script:
```bash
python read_data.py
```

Stop and remove container:
```bash
docker stop pg-container
docker rm pg-container
```

---

## 📁 Project Structure

```
pydocker/
├── README.md                      # This file - Project overview
├── DOCKER_INSTALLATION_GUIDE.md   # Docker installation steps for macOS
├── POSTGRES_SETUP.md              # PostgreSQL setup guide
├── TROUBLESHOOTING.md             # Common issues & solutions
├── init.sql                       # SQL initialization script (optional)
├── requirements.txt               # Python dependencies (psycopg)
├── read_data.py                   # Python script to read data
├── read.ipynb                     # Jupyter notebook example
└── .gitignore                     # Git ignore file
```

---

## 💻 Usage Examples

### Connect to PostgreSQL via Terminal

```bash
docker exec -it pg-container psql -U postgres -d testdb
```

### Create Table and Insert Data

```sql
CREATE TABLE names (
    firstname VARCHAR(100),
    lastname VARCHAR(100)
);

INSERT INTO names (firstname, lastname) VALUES
    ('Meenakshi', 'Sethi'),
    ('Bajrangi', 'Gupta');
```

### Query Data

```sql
SELECT * FROM names;
```

### Python Connection Example

```python
import psycopg

conn = psycopg.connect(
    dbname='testdb',
    user='postgres',
    password='postgres',
    host='localhost',
    port=5487
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM names")
print(cursor.fetchall())

cursor.close()
conn.close()
```

---

## 🛠️ Troubleshooting

Common issues I encountered and how I solved them:

### Issue 1: Port Already in Use
**Error:** `bind: address already in use`  
**Solution:** Use a different host port: `-p 5487:5432`

### Issue 2: pgAdmin Role Error
**Error:** `role "postgres" does not exist`  
**Solution:** Verify username in pgAdmin matches the POSTGRES_USER

### Issue 3: psycopg2 Not Working on Python 3.13
**Error:** Build failures with psycopg2-binary  
**Solution:** Use psycopg3: `pip install "psycopg[binary]>=3.1.0"`

**For complete troubleshooting guide:** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## 📚 What I Learned

### Key Takeaways:

1. **Port Mapping Format:** `HOST_PORT:CONTAINER_PORT`
   - Container port is always `5432` for PostgreSQL
   - Host port can be any available port (5432, 5487, etc.)

2. **psycopg2 vs psycopg3:**
   - psycopg2 uses `database` parameter
   - psycopg3 uses `dbname` parameter

3. **Docker Container Management:**
   - Always check if container is running: `docker ps`
   - View logs: `docker logs pg-container`
   - Restart: `docker restart pg-container`

4. **pgAdmin Connection:**
   - Username must match POSTGRES_USER
   - Port must match the host port (left side of mapping)
   - Use 127.0.0.1 or localhost

---

## 📝 Database Details

| Parameter | Value |
|-----------|-------|
| Host | localhost |
| Port | 5487 |
| Database | testdb |
| Username | postgres |
| Password | postgres *(for demo only)* |
| Table | names (firstname, lastname) |

> **⚠️ Security Note:** The credentials used in this project (`postgres`/`postgres`) are for **demonstration and local development only**. For production environments, always use strong passwords and store them securely using environment variables or secret management tools.

---

## � Insert and Read Records with Python

### Complete Example: Read, Insert, and Verify

The `read_data.py` script demonstrates a complete workflow:

```python
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
    
    # Read 1 record
    cursor.execute("SELECT firstname, lastname FROM names LIMIT 1")
    record = cursor.fetchone()
    print(f"First Name: {record[0]}, Last Name: {record[1]}")
    
    # Insert 2 new records
    cursor.execute("INSERT INTO names (firstname, lastname) VALUES (%s, %s)", ('John', 'Doe'))
    cursor.execute("INSERT INTO names (firstname, lastname) VALUES (%s, %s)", ('Jane', 'Smith'))
    conn.commit()
    print("Inserted 2 new records")
    
    # Read all records
    cursor.execute("SELECT * FROM names")
    all_records = cursor.fetchall()
    print(f"Total records: {len(all_records)}")
    for record in all_records:
        print(f"  - {record[0]} {record[1]}")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Error: {e}")
```

### Key Points:
- ✅ Always use parameterized queries (`%s`) to prevent SQL injection
- ✅ Call `conn.commit()` after INSERT/UPDATE/DELETE operations
- ✅ Use `fetchone()` for single records, `fetchall()` for multiple records
- ✅ `SELECT *` fetches all columns from the table

### VS Code Setup

To avoid Python interpreter issues with the Run button, create `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "/opt/anaconda3/bin/python3"
}
```

This ensures VS Code always uses the correct Python environment with psycopg installed.

---

## �🙏 Acknowledgments

- Docker Documentation
- PostgreSQL Documentation
- psycopg Documentation
- ChatGPT for troubleshooting assistance

---

## 📄 License

This project is open source and available for educational purposes.

---

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements or additional examples!

---

**Happy Coding! 🚀**
