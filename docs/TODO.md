# TODO LIST
pip uninstall psycopg2
---
# 🚩F1 Backend Core Development

### ✓ level 1 complete core
### ✓ level 2 complete account
### ✓ level 3 complete ContactUs
### ✓ level 4 complete public
### ✓ level 5 rosetta


-----

# 🚩 F2 — Frontend Development with Tailwind

### ✓ Step 1: Tailwind installation and setup
### ✓ Step 2: build base layout and structure
### ✓ Step 3: apply basic styling with Tailwind
### ✓ Step 4: clean code and UI structure (apply @apply, reuse styles)
### ✓ Step 5: add all translation blocks ({% trans %} / {% blocktrans %})
### ✓ Step 6: UI final QA + minor SEO structure

-----

# 🚩 F3 — Advanced Systems & DevOps

### ✓ Step 1: Write Dockerfile + .dockerignore
### ✓ Step 2: Define docker-compose.yml (web, db, redis, celery)
### ✓ Step 3: Test container-based execution (web + db)
### ✓ Step 4: Setup Celery Worker/Beat with Redis
### ✓ Step 5: Implement async task (ContactUs email)
### ✓ Step 6: Setup proper logging (Celery + Django + Docker)


## 🔧 F4 — Finalize Production-Ready Dockerized System and deploy 

### ✅ Step 1: Run in production mode and verify all systems
- [✓] Run docker compose up --build without debug tools
- [✓] Test static and media files are served via nginx
- [✓] Ensure Gunicorn starts from entrypoint correctly
- [✓] Confirm Celery worker and beat are active
- [✓] Open Flower UI at localhost:5555 and check status
- [✓] Send test ContactUs form to validate async task
- [✓] Monitor system logs (docker compose logs -f)
- [✓] Use docker stats or htop for performance snapshot

### 🔁 Step 2: Cleanup & Final Docker image
- [✓] Add production .env variables
- [✓] Optimize image layers if needed
- [✓]Tag image for deployment
- [✓] Push to private registry (if using)

### 🌐 Step 3: Setup domain and Nginx for live use
- [✓] Buy or assign domain
- [✓] Point DNS to server IP
- [✓] Configure Nginx to route traffic
- [✓] Test site publicly on HTTP (port 80)

### 🔐 Step 4: Enable HTTPS with Let’s Encrypt
- [✓] Install certbot inside or outside container
- [✓] Update Nginx config to handle HTTPS
- [✓] Verify SSL cert renewal automation

### 📦 Step 5: Production Deployment & Smoke Test
- [✓] Deploy full stack on production VPS
- [✓] Run smoke test (basic routes, async, login if exists)
- [✓] Confirm logs and system health
- [✓] Document all production URLs and secrets