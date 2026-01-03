# Docker Volumes - Data Persistence Guide

## Understanding Data Storage in Docker

### Current Setup (Without Volumes)
When you run:
```bash
docker run --name pg-container \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=testdb \
  -p 5487:5432 \
  -d postgres
```

**Data location:** Inside the container's filesystem (Docker's internal storage)

**What happens:**
- ✅ `docker stop` → Data preserved
- ❌ `docker rm` → **Data LOST forever**

---

## Using Volumes for True Data Persistence

### Option 1: Named Volume (Recommended)

Create a named volume that persists even if you remove the container:

```bash
# Create a named volume
docker volume create postgres_data

# Run container with volume
docker run --name pg-container \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=testdb \
  -p 5487:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  -d postgres
```

**Benefits:**
- ✅ Stop container → Data safe
- ✅ Remove container → Data **still safe** in volume
- ✅ Create new container with same volume → Data restored

**Managing volumes:**
```bash
# List volumes
docker volume ls

# Inspect volume
docker volume inspect postgres_data

# Remove volume (only when you want to delete data)
docker volume rm postgres_data
```

---

### Option 2: Bind Mount (Local Folder)

Store data in a folder on your Mac:

```bash
# Create a local folder for data
mkdir -p ~/docker-postgres-data

# Run container with bind mount
docker run --name pg-container \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=testdb \
  -p 5487:5432 \
  -v ~/docker-postgres-data:/var/lib/postgresql/data \
  -d postgres
```

**Benefits:**
- ✅ Data stored in `~/docker-postgres-data`
- ✅ You can see the files on your Mac
- ✅ Easy to backup (just copy the folder)

---

## Migrating Your Current Container to Use Volumes

If you already have data in your current container and want to preserve it:

### Step 1: Backup your data
```bash
# Export your database
docker exec pg-container pg_dump -U postgres testdb > backup.sql
```

### Step 2: Stop and remove old container
```bash
docker stop pg-container
docker rm pg-container
```

### Step 3: Create volume and new container
```bash
# Create named volume
docker volume create postgres_data

# Run new container with volume
docker run --name pg-container \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=testdb \
  -p 5487:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  -d postgres

# Wait a few seconds for PostgreSQL to start
sleep 5
```

### Step 4: Restore your data
```bash
# Import the backup
docker exec -i pg-container psql -U postgres -d testdb < backup.sql
```

### Step 5: Verify
```bash
docker exec -it pg-container psql -U postgres -d testdb -c "SELECT * FROM names;"
```

---

## Data Persistence Comparison

| Scenario | Without Volume | With Volume |
|----------|----------------|-------------|
| `docker stop` | ✅ Data kept | ✅ Data kept |
| `docker start` | ✅ Data restored | ✅ Data restored |
| `docker rm` | ❌ Data LOST | ✅ Data kept in volume |
| `docker rm -v` | ❌ Data LOST | ❌ Data LOST (removes volume) |
| Reinstall Docker | ❌ Data LOST | ✅ Data kept |

---

## Using init.sql with Volumes

To automatically initialize your database with the init.sql file:

```bash
docker run --name pg-container \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=testdb \
  -p 5487:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  -v $(pwd)/init.sql:/docker-entrypoint-initdb.d/init.sql \
  -d postgres
```

**Note:** `init.sql` only runs on **first startup** when the database is empty.

---

## Best Practices

1. **For Development:** Use named volumes (`docker volume create`)
2. **For Production:** Use named volumes with regular backups
3. **For Backups:** Use bind mounts or export with `pg_dump`
4. **Always backup** before removing volumes

---

## Quick Reference

```bash
# Create volume
docker volume create postgres_data

# Run with volume
docker run --name pg-container \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=testdb \
  -p 5487:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  -d postgres

# Backup database
docker exec pg-container pg_dump -U postgres testdb > backup.sql

# Restore database
docker exec -i pg-container psql -U postgres -d testdb < backup.sql

# Remove container (data safe in volume)
docker rm -f pg-container

# Remove volume (permanently delete data)
docker volume rm postgres_data
```
