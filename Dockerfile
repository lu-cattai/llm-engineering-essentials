# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables to prevent Python from writing pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies required for C++ compilation and performance monitoring
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
# Note: pybind11 is needed for the C++ bridge
RUN pip install --no-cache-dir pybind11 psutil

# Copy the current directory contents into the container at /app
COPY . .

# Documentation: This container is designed to run benchmarking and performance tests
# In a real scenario, we would compile the .cpp module here
# RUN c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) memory_manager.cpp -o performance_lib$(python3-config --extension-suffix)

# Default command to run the performance benchmarker
CMD ["python", "benchmarker.py"]