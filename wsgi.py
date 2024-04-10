import sys
from pathlib import Path

# Add the project directory to the Python path
project_dir = Path(__file__).resolve().parent
sys.path.append(str(project_dir))

print(f"\n[WSGI] - Project directory: {project_dir}")

# Import the API object from the main module
from src.main import api

# print project_dir
print(f"\n[WSGI] - api: {api}\n")

# Create the WSGI application
application = api