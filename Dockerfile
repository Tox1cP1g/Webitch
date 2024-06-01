# Use the official Python image as the base image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /Webitch

# Install dependencies
COPY requirements.txt /Webitch
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install requests


# Copy the Django project into the container
COPY . /Webitch/

# Run the Django project
CMD ["python3", "manage.py", "runserver"]