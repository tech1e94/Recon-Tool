#!/bin/bash

# Create a virtual environment named 'myenv'
python3 -m venv ~/myenv

# Activate the virtual environment
source ~/myenv/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install the required Python packages from requirements.txt
pip install -r requirements.txt

# Indicate that the environment has been set up
echo "Virtual environment 'myenv' created and all packages installed."
