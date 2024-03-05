# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /code
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable for Django
ENV DJANGO_SETTINGS_MODULE=restapi.settings

# Create and apply migrations, and create a superuser
CMD python manage.py createsuperuser && \
    python manage.py migrate && \
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell && \
    python manage.py runserver 0.0.0.0:8000