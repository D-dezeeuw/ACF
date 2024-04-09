import sys
from pathlib import Path

# Add the project directory to the Python path
project_dir = Path(__file__).resolve().parent
sys.path.append(str(project_dir))

# Import the API object from the main module
from src.main import api

# Create the WSGI application
application = api