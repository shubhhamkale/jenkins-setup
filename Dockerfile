FROM python:3.9-slim
# Use an official Python runtime as a base image



# Set the working directory in the container
WORKDIR /app

# Copy the contents of the current directory to the container's working directory
COPY . /app

# Install pytest, pytest-html, and requests
RUN pip install pytest pytest-html requests

# Set the entry point to the Python script
ENTRYPOINT ["python", "report.py"]
