#!/bin/bash

# Create a new virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required dependencies
venv/bin/python3 -m pip install -r requirements.txt

# Check if the installation was successful
if [ $? -eq 0 ]; then
    echo "Dependencies installed successfully."
    
    # Start the server
    bash ./runserver.sh
else
    echo "Failed to install dependencies. Please check the requirements.txt file and try again."
fi