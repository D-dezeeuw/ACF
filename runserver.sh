#!/bin/bash

export PYTHONPATH=$PYTHONPATH:$(pwd)
uvicorn wsgi:application