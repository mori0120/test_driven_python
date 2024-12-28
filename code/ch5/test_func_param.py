import pytest
from cards import Card

@pytest.mark.parametrize('start_summary, start_state', [
    ("Write code", "done"),
    ("Write code2", "in prog"),
    ("Write code3", "todo"),
])
def test_finish(cards_db, start_summary, start_state):
    index = cards_db.add_card(Card(summary=start_summary, state=start_state))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"

@pytest.mark.parametrize('start_state', ["in prog", "done", "todo"])
def test_finish_simple(cards_db, start_state):
    c = Card(summary="Write code", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"