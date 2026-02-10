FROM python:3.14-slim

WORKDIR /code

# System dependencies for Postgres
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all project files
COPY . /code/

EXPOSE 8000
