FROM astral/uv:python3.13-trixie-slim

# Set work directory
WORKDIR /app

# Copy requirements and app
COPY requirements.txt .
COPY app.py .

# Install dependencies
RUN uv pip install -r requirements.txt --no-cache-dir --system

# Clean Cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && uv cache prune 

# Expose port
EXPOSE 8521

# Run FastAPI app with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8521"]