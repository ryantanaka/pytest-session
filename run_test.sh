#!/bin/bash 

export PYTHONPATH=$(pwd)/src
$(pwd)/venv/bin/pytest --cov-report term --cov-report html --cov=src
