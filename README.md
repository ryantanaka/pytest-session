# pytest-session

This repo is organized as follows:

```
.
├── src
│   ├── __init__.py
│   └── main.py      <--- source code
└── test
    └── test_main.py <--- unit testing code 
```

The following instructions detail how you can run this set of sample PyTest unit tests from a Linux/Unix terminal.

Alternatively you can use a terminal through our hosted jupyter notebooks: 
https://docs.google.com/document/d/19m3zrA5X7R9vEsEExAMPayzt4ydfy7IoBoGBkxKB1OM/edit. To use this, click on the link
next to your name and enter the password. On the top right, you will see `New`. Click on `New`, then `Terminal` to open
up a terminal that you can use for the following instructions. 

## Usage

1. `git clone https://github.com/ryantanaka/pytest-session.git` <-- obtain this repo containing the sample test code 
2. `cd pytest-session` <-- change your current working directory to be the `pytest-session` directory where the test code resides
3. `pip3 install --user pytest pytest-cov` <-- install the pytest dependencies
4. `export PYTHONPATH=$(pwd)/src` <-- set `PYTHONPATH` to point to the directory where our source code resides (the code we will test)
5. `python3 -m pytest --cov-report term --cov-report html --cov=src` <-- run pytest, which will run the unit tests defined in `test/test_main.py`

If you run this on your own machine, you can look at `htmlcov/index.html` to see the code coverage report via a browser. 

