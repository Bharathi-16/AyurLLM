# ============================================
# AyurParam AI — Production Dockerfile (GPU)
# ============================================
FROM nvidia/cuda:12.1.1-runtime-ubuntu22.04

# Prevent interactive prompts during package install
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install Python 3.11
RUN apt-get update && apt-get install -y \
    python3.11 python3.11-venv python3-pip \
    curl git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set Python 3.11 as default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1

WORKDIR /app

# Install Python dependencies first (for Docker cache efficiency)
COPY requirements-prod.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements-prod.txt

# Copy project files
COPY app/ ./app/
COPY templates/ ./templates/
COPY run.py .
COPY gunicorn.conf.py .

# Create data directory for SQLite
RUN mkdir -p /app/data /app/logs

# Expose port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:8080/api/status || exit 1

# Run with Gunicorn (production server)
CMD ["gunicorn", "--config", "gunicorn.conf.py", "run:app"]
