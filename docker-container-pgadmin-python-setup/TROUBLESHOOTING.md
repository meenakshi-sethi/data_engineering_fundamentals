# Troubleshooting Guide

Common issues and solutions when working with Docker and PostgreSQL.

---

## ❌ Issue 1: Port Already in Use

### Error Message:
```
docker: Error response from daemon: ports are not available: 
exposing port TCP 0.0.0.0:5432 -> 127.0.0.1:0: listen tcp 0.0.0.0:5432: 
bind: address already in use
```

### What Happened:
Port 5432 on your Mac is already being used by another application (maybe another PostgreSQL instance or another container).

### ✅ Solution 1: Use a Different Port

Change the **host port** (left side) to an available port like 5433, 5434, or 5487:

```bash
docker run --name pg-container \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=testdb \
  -p 5487:5432 \
  -d postgres
```

**Important:** Port mapping is `HOST_PORT:CONTAINER_PORT`
- Container port is always **5432** (PostgreSQL default inside container)
- Host port can be anything available on your Mac

### ✅ Solution 2: Find and Stop the Process Using the Port

Find what's using port 5432:
```bash
lsof -i :5432
```

Stop the process if needed or use a different port.

### ✅ Solution 3: Remove Existing Container

If you already have a container using that port:

```bash
docker ps -a  # List all containers
docker rm -f pg-container  # Remove the container
```

Then run your docker command again.

---

## ❌ Issue 2: pgAdmin Connection Error - "Role does not exist"

### Error Message:
```
connection failed: connection to server at "127.0.0.1", port 5432 failed: 
FATAL: role "postgres" does not exist
```

### What Happened:
You might have entered the wrong username in pgAdmin or the PostgreSQL user wasn't created properly.

### ✅ Solution: Verify User Exists

1. **Connect to the container:**
```bash
docker exec -it pg-container psql -U postgres -d testdb
```

2. **List all roles:**
```sql
\du
```

You should see:
```
 Role name |                         Attributes                         
-----------+------------------------------------------------------------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS
```

3. **In pgAdmin, use these settings:**
   - **Host:** localhost or 127.0.0.1
   - **Port:** 5487 (or whatever you mapped)
   - **Database:** testdb
   - **Username:** postgres
   - **Password:** postgres

---

## ❌ Issue 3: Cannot Connect from Python

### Error Message:
```python
ModuleNotFoundError: No module named 'psycopg'
```

### ✅ Solution:
Install psycopg in your Python environment:

```bash
pip install "psycopg[binary]>=3.1.0"
```

Make sure you're using the **same Python environment** where you installed psycopg.

---

## ❌ Issue 4: Wrong Connection Parameter in psycopg3

### Error Message:
```
invalid connection option "database"
```

### What Happened:
psycopg2 uses `database` parameter, but **psycopg3 uses `dbname`**.

### ✅ Solution:
Change your connection code:

**Wrong (psycopg2):**
```python
conn = psycopg.connect(database='testdb', ...)
```

**Correct (psycopg3):**
```python
conn = psycopg.connect(dbname='testdb', ...)
```

---

## ❌ Issue 5: Container Stops Immediately After Starting

### Check Container Logs:
```bash
docker logs pg-container
```

Common causes:
- Invalid environment variables
- Port conflict
- Insufficient permissions

### ✅ Solution:
Remove the container and recreate with correct settings:
```bash
docker rm -f pg-container
docker run --name pg-container \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=testdb \
  -p 5487:5432 \
  -d postgres
```

---

## ❌ Issue 6: Python 3.13 Incompatibility with psycopg2-binary

### Error Message:
```
error: command '/usr/bin/clang' failed with exit code 1
```

### What Happened:
psycopg2-binary has compatibility issues with Python 3.13.

### ✅ Solution:
Use **psycopg3** instead:

```bash
pip install "psycopg[binary]>=3.1.0"
```

Update your import:
```python
import psycopg  # Not psycopg2
```

---

## ❌ Issue 7: Port Mapping Confusion

### Common Mistake:
```bash
-p 5433:5433  # ❌ WRONG
```

### ✅ Correct Understanding:

**Format:** `-p HOST_PORT:CONTAINER_PORT`

- **Container port:** Always **5432** for PostgreSQL (this is inside the Docker container)
- **Host port:** Can be any available port on your Mac (5432, 5433, 5487, etc.)

**Examples:**
```bash
-p 5432:5432  # Mac port 5432 → Container port 5432
-p 5487:5432  # Mac port 5487 → Container port 5432
-p 8000:5432  # Mac port 8000 → Container port 5432
```

---

## Need More Help?

- Check [Docker Documentation](https://docs.docker.com/)
- Check [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- Check [psycopg Documentation](https://www.psycopg.org/psycopg3/docs/)
