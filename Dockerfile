# ==================================
# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /usr/src/swarms


# Install Python dependencies
# COPY requirements.txt and pyproject.toml if you're using poetry for dependency management
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY scripts /app/scripts
COPY swarms /app/swarms
COPY example.py /app/example.py

# Copy the rest of the application
COPY . .
# Make port 80 available to the world outside this container
#EXPOSE 80

# Define environment variable
# ENV NAME World
# ENV OPENAI_API_KEY=your_swarm_api_key_here
# Run app.py when the container launches
CMD ["python3", "example.py"]

