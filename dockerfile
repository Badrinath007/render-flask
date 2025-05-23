# Use an official Python runtime as a parent image
FROM python:3.12-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define the command to run the application
# Use gunicorn to serve the Flask app, as recommended for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
