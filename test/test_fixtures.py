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

