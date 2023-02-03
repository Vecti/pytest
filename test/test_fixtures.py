### fixtures: sometimes we want to 'reuse; some component of test
##3 we define function, in arguments if name match with fixture set, it run those fixtures, captures what they ruturn, move further

# so tine save
#  fixtures can be arguments, METHODS, FUNCITONS, class- wooww


# how we can use this
# define the 'env list' as fixture - so we can chekc if we have this or not


### second:
### define state

## plusy
## fixtures can divide our work into more cleaned one and so on, fixture in fixture
## reusable - and safe
## multiple reusable
## FIXTURES DOES NOT NEED TO HAVE THOSE STUPID TEST IN NAME
## fixtures can run /return modules

## minusy
## fixture cant get an argument - so you have to use them differently
## assume fixtures should not do assertione tc

## can be used everywhere

import pytest
import numpy as np

## scope: if class/modelu/package/sessions - execute it ONCE per it
## so here - everytime will be drawn the same (like random.seed)

# but looks like it needs to be imported

@pytest.fixture(scope='session')
def i_draw_card():
    card_options = [2,3,4,5]
    return np.random.choice(card_options)

@pytest.fixture(scope='session')
def opponent_draw_card():
    card_options = [2,3,4,5]
    return np.random.choice(card_options)

#TODO

#understand tearup order/structure
## 'introstpect the equesting  test context'

## factories as fixture 

@pytest.fixture
def make_customer_record():
    """
    The “factory as fixture” pattern can help in situations where the result of a fixture
    is needed multiple times in a single test. Instead of returning data directly,
    the fixture instead returns a function which generates the data.
    This function can then be called multiple times in the test.

    Important - we can provide a parameters there
    like factory DP? we can generate objects?
    """
    
    def _make_customer_record(name):
        return {"name": name, "orders": []}

    return _make_customer_record


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")