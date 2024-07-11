import pytest
from blackjack.common import card_score

@pytest.mark.parametrize("cards,score", [('KK',20),('JKQ',0),('KA',21),('AA',12)])
def test_simple_case(cards,score):
  assert card_score (cards) == score  

def test_value_error_is_raised():
  with pytest.raises(ValueError):
    #card_score("")
    card_score(1)