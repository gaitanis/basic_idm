# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /workdir
WORKDIR /workdir

# Install any needed packages specified in requirements.txt
COPY requirements.txt /workdir
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80
EXPOSE 4000

# Copy the current directory contents into the container at /workdir
ADD *.py /workdir/

RUN mkdir /workdir/templates && \
    mkdir /workdir/static && \
  	mkdir /workdir/static/js

ADD static/js/* /workdir/static/js/
ADD templates/* /workdir/templates/

ENV PORT 80
ENV APP_URL http://user

# Run app.py when the container launches
CMD ["python", "web.py"]
