import pytest

@pytest.mark.onlyme
class TestClass:
    """
    those will be executed via keyword onlyme
    """
    def func(self, x):
        return x + 1

    def test_answer(self):
        assert self.func(3) == 4


