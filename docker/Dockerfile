# Use Python 3.11 as base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Security: Create non-root user
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

# Copy requirements first (for better caching)
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Switch to non-root user
USER appuser

# Expose port 5000
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:5000/health || exit 1

# Run the app with gunicorn (production server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]