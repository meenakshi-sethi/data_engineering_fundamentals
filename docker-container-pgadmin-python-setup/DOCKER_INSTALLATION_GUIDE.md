# Docker Installation Guide for macOS (M1/M2/M3)

## Step 1: Check your Mac type

1. Click **Apple menu** → **About This Mac**
2. Check your chip:
   - **Apple chip** → Apple M1 / M2 / M3 → **Apple Silicon**
   - **Intel chip** → **Intel**

## Step 2: Download Docker Desktop

Go to: 👉 [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

Download the correct version:
- **Docker Desktop for Mac (Apple Silicon)** - for M1/M2/M3
- **Docker Desktop for Mac (Intel)** - for Intel Macs

## Step 3: Install Docker Desktop

1. Open the downloaded `.dmg` file
2. Drag **Docker.app** → **Applications** folder
3. Open **Docker** from Applications
4. Grant permissions when asked
5. Wait until Docker says **"Docker is running"**

You'll see a 🐳 icon in the menu bar when it's running.

## Step 4: Verify Installation

Open **Terminal** and run:

```bash
docker --version
```

**Expected output:**
```
Docker version XX.XX.X, build XXXXX
```

Test Docker is working:
```bash
docker ps
```

If you see no errors, you're all set! 🎉

---

## Next Steps

Once Docker is installed, you can proceed to:
- [Setting up PostgreSQL with Docker](POSTGRES_SETUP.md)
- Running the example notebooks and scripts in this repository
