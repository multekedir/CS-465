# test_encode.py:

from encode import encode


def test_empty_string():
    assert encode("") == ""


def test_normal_string():
    assert encode("ad") == "ad"


def test_normal_string():
    assert encode("ad") == "ad"


def test_compressed_string():
    assert encode("Aabb") == "Aab2"
    assert encode("AAb") == "A2b"
