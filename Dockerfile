# Use an official Python image as the base
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app/

# Expose the port
EXPOSE 8000

# Run the command to start the development server
CMD ["uvicorn", "app/api:app", "--host", "0.0.0.0", "--port", "8000"]