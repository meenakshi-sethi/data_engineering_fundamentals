# PostgreSQL Setup with Docker

Complete guide to setting up PostgreSQL using Docker and connecting via terminal.

## ✅ Step 0: Ensure Docker is Running

Check the 🐳 icon in the menu bar.

Verify Docker is working:
```bash
docker ps
```

(No error = good!)

---

## Step 1: Pull PostgreSQL Image

Download the official PostgreSQL image from Docker Hub:

```bash
docker pull postgres
```

---

## Step 2: Run PostgreSQL Container

Create and run a PostgreSQL container with the following configuration:
- **Username:** postgres
- **Password:** postgres
- **Database:** testdb
- **Port:** 5432 (default) or 5487 (if 5432 is in use)

```bash
docker run --name pg-container \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=testdb \
  -p 5487:5432 \
  -d postgres
```

### 📌 Command Breakdown:
- `--name pg-container` → Name of the container
- `-e` → Environment variables (username, password, database)
- `-p 5487:5432` → Port mapping (HOST_PORT:CONTAINER_PORT)
  - `5487` = Port on your Mac
  - `5432` = Port inside the container (PostgreSQL default)
- `-d` → Run in detached mode (background)
- `postgres` → Image name

---

## Step 3: Verify Container is Running

Check if your container is running:

```bash
docker ps
```

You should see `pg-container` in the list.

---

## Step 4: Connect to PostgreSQL

### Method 1: Via Terminal (Inside Container)

This is the most reliable way to connect:

```bash
docker exec -it pg-container psql -U postgres -d testdb
```

If successful, you'll see:
```
testdb=#
```

🎉 You are now inside PostgreSQL!

### Method 2: From Your Mac (Local Connection)

Connect using psql installed on your Mac:

```bash
psql -h localhost -p 5487 -U postgres -d testdb
```

---

## Step 5: Create Table and Insert Data

Once connected to PostgreSQL, run these commands:

### Create the table:
```sql
CREATE TABLE names (
    firstname VARCHAR(100),
    lastname VARCHAR(100)
);
```

### Insert data:
```sql
INSERT INTO names (firstname, lastname) VALUES
    ('Meenakshi', 'Sethi'),
    ('Bajrangi', 'Gupta');
```

### Verify data:
```sql
SELECT * FROM names;
```

Expected output:
```
 firstname  | lastname
------------+----------
 Meenakshi  | Sethi
 Bajrangi   | Gupta
(2 rows)
```

---

## Common Container Commands

### Start the container:
```bash
docker start pg-container
```

### Stop the container:
```bash
docker stop pg-container
```

### Remove the container:
```bash
docker rm pg-container
```

### View container logs:
```bash
docker logs pg-container
```

---

## Next Steps

- [Troubleshooting Common Issues](TROUBLESHOOTING.md)
- [Connect to Python using psycopg](README.md#connecting-to-python)
