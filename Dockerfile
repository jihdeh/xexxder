# We Use an official Python runtime as a parent image
FROM python:3


# Setting PYTHONUNBUFFERED to a non empty value ensures that the python output is sent straight to terminal (e.g. your container log) 
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /sennder

# Set the working directory
WORKDIR /sennder

# Copy the current directory contents into the container
ADD . /sennder/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
