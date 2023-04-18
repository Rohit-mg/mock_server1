# Use an official Python runtime as a parent image
# FROM amd64/python:3.10.11-buster(mock,rohitmg/mock_server)
# FROM python:3.10.11-buster(mock_arm)
FROM amd64/python:3.10.11-buster

RUN apt-get update && apt-get install -y curl

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
# COPY requirements.txt .
COPY . .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
# COPY . .



# Expose the port on which the app will run
# EXPOSE 2000

# Run the command to start the app
CMD ["python3","app.py"]