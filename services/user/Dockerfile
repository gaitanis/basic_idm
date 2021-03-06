# Use an official Python runtime as a parent image
#FROM python:3.6-slim
FROM gliderlabs/alpine:3.4

# Set the working directory to /workdir
WORKDIR /workdir

RUN apk add --no-cache \
    mysql-client \
    mariadb-dev \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install --upgrade pip \
  && pip install virtualenv

# Install any needed packages specified in requirements.txt
COPY requirements.txt /workdir
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80
EXPOSE 3306

# Copy the current directory contents into the container at /workdir
ADD *.py /workdir/

# Define environment variable
ENV NAME World
ENV PORT 80

# Run app.py when the container launches
CMD ["python", "user.py"]
