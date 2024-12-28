import pytest
from cards import Card

@pytest.fixture(params=["in prog", "done", "todo"])
def start_state(request):
    return request.param

def test_finish(cards_db, start_state):
    index = cards_db.add_card(Card(summary="Write code", state=start_state))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"