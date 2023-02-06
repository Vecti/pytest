from test_fixtures import *
## conftest.py per project/subfolder -> if placed there we dont need to import fixtures

def test_types(i_draw_card, opponent_draw_card):

    print(type(i_draw_card))
    assert i_draw_card == int(i_draw_card)
    assert opponent_draw_card == int(opponent_draw_card)
    print('test_types me', i_draw_card)
    print('test_types opp', opponent_draw_card)
    assert i_draw_card < opponent_draw_card


def test_draws(i_draw_card, opponent_draw_card):
#     assert isinstance(i_draw_card, int) == 1
#     assert isinstance(opponent_draw_card, int) == 1
    assert i_draw_card == int(i_draw_card)
    assert opponent_draw_card == int(opponent_draw_card)
    print('test_draws me', i_draw_card)
    print('test_draws opp', opponent_draw_card)
    assert i_draw_card > opponent_draw_card