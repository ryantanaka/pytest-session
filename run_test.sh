#!/bin/bash 

python3 -c "import pytest" &> /dev/null
if [ "$(echo $?)" -eq 1 ]
then
    pip3 install --user pytest pytest-cov
fi

export PYTHONPATH=$(pwd)/src
python3 -m pytest --cov-report term --cov-report html --cov=src
