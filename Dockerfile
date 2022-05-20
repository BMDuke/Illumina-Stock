# Select base image
FROM python:3

# Install deps

# Set up the working environment
RUN mkdir /app
WORKDIR /app

# Set up alias to handle credentials
