# --- Stage 1: The Builder ---
FROM python:3.10-slim as builder

WORKDIR /build

# Install build tools temporarily
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install to a local folder
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# --- Stage 2: The Final Runtime ---
FROM python:3.10-slim

WORKDIR /app

# Install only the runtime library needed for FAISS (much smaller than build-essential)
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy only the installed packages from the builder stage
COPY --from=builder /root/.local /root/.local
COPY . .

# Set paths so Python can find the libraries
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUSERBASE=/root/.local

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]









# FROM python:3.11-slim

# WORKDIR /app

# #installing dependency for fiass and pdf processing
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libssl-dev \
#     && rm -rf /var/lib/apt/lists/*

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# EXPOSE 8000

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]




# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Set working directory
# WORKDIR /app

# # Install system dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#     libssl-dev \
#     curl \
#     && rm -rf /var/lib/apt/lists/*

# # Copy the requirements first to leverage Docker cache
# COPY requirements.txt .

# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Pre-download the embedding model so it's ready when the container starts
# RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

# # Copy remaining application code
# COPY . .

# # Expose the port the application runs on
# EXPOSE 8000

# # Run the application
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]