from password_hw2 import is_password_reliable
import pytest

@pytest.mark.parametrize("password,expected", [
    ("     ", False),
    ("aaa", False),
    ("1a#", False),
    ("fffffff55555", False),
    ("aaaa 1111 %%%%", False),
    ("********************************", False),
    ("", False),
    ("a0^00000000000", True),
    ("HHHHHhhhhh*****000000", True),
    ("password123#", True)
])
def test_is_password_reliable(password, expected):
    actual = is_password_reliable(password)
    assert expected is actual

@pytest.mark.skip(reason="Test is not ready yet")
def test_password_symbol_diversity():
    pass