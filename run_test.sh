#!/bin/bash 

export PYTHONPATH=$(pwd)/src
pytest --cov-report term --cov-report html --cov=src
