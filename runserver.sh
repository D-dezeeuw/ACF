#!/bin/bash

export PYTHONPATH=$PYTHONPATH:$(pwd)
echo "Starting WSGI Server."

uvicorn wsgi:application --host 0.0.0.0 --port 8000 --log-level debug