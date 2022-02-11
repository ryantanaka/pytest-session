#!/usr/bin/env python3
import pytest

from main import increment

def test_increment():
    assert increment(1) == 2

def test_increment_bad_type():
    with pytest.raises(TypeError) as e:
        increment("hi")

    print(str(e))

#https://www.ibm.com/topics/software-testing
