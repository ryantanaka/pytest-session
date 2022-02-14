#!/bin/bash 

python3 -c "import pytest" &> /dev/null
if [ "$(echo $?)" -eq 1 ]
then
    pip3 install pytest pytest-cov
fi

export PYTHONPATH=$(pwd)/src
pytest --cov-report term --cov-report html --cov=src
