# test_encode.py:

from encode import encode


def test_empty_string():
    assert encode("") == ""


def test_normal_string():
    assert encode("ad") == "ad"
