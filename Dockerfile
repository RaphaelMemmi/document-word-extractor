# Use official Python image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose port 8000 for Django server
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
