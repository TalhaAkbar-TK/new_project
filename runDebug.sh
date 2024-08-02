#!/bin/bash

# Set environment variables
export DB_NAME=retail
export DB_URL=localhost
export DB_USER=server-ere  # Replace with your PostgreSQL username
export DB_PWD=talha
export DB_PORT=5432  # Default PostgreSQL port

# Run the Flask application
python runDebug.py
