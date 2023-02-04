# parametrziation: so we can provide list  of arguments/fixtures/ components to test
# also fixtures does not need to have test in name - dziz
# here with 'factory ficture' - ficture returns functions which generate a data

import pytest


## fixtures  - think of way as POINT 1 = arrange - this way WE arrange those data which we need
## executed everytime when provided
## but if we provide different scope -> then not!/or reused


## way 1 - just fixture

@pytest.fixture()
def show_dividers_naive():
    number = 10
    return [i for i in range(1, number) if number%i==0]

def test_if_ten_work(show_dividers_naive):
    assert show_dividers_naive == [1,2,5]


## 'factory' - this way we can test faster and mmore
##


@pytest.fixture()
def show_dividers_factory():
    def _show_dividers_factory(number):
        return [i for i in range(1, number) if number%i==0]
    return _show_dividers_factory


def test_if_numbers_works(show_dividers_factory):
    value_1 = show_dividers_factory(6)
    value_2 = show_dividers_factory(12)
    value_3 = show_dividers_factory(18)
    assert value_1 == [1,2,3]
    assert value_2 == [1,2,3,4,6]
    assert value_3 == [1,2,3,6,9]
    

## just mark parametrization and nice - EACH TEST SEPARATLY
@pytest.mark.parametrize("test_input, expected", [(6, [1,2,3]), (12, [1,2,3,4,6]), (18, [1,2,3,6,9])])
def test_eval(test_input, expected):
    assert [i for i in range(1, test_input) if test_input%i==0] == expected


### forth way - we can parametrize fixtures but i fk up constuctions
## one fixtures - provides 6, second 12, third 18 
## and fixtures which in params - answers? and test separate
