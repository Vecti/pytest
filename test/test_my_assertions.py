import pytest


# so with pytest.raises -> it captures the error but IT PASS THIS TEST?
# so how wecan know about it even?
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
    # return 1 / 0

def test_jazda():
    assert a % 2 == 0, "value was odd, should be even"
