# https://docs.pytest.org/en/7.2.x/how-to/mark.html#mark
## pytest --markersc

## wortf to know


## skip - as name suggest
## can be applied on class also
import pytest
import sys


def test_dip():
    assert 2 ==3

# pytestmark - global / everything in module acti/dis
# so either everywhere make decorators or here append/overwrite


@pytest.mark.skip(reason='can`t be tested here')
def test_fail():
    assert 3 < 0

## skipif - 

@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
def test_linux_fail():
    assert 1==0



### HERE PROBABLY USED INPROPERLY - if commented - whole file skipped
### probably  .importorskip should be used inside test?

# docutils = pytest.importorskip("makaron")
# import makaron


# xfails - expected fails, similar we can provide conditions etc

@pytest.mark.xfail(reason='poorly writen test :)')
def test_function():
    assert 1/0


