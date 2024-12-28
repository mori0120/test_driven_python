from cards import Card

def pytest_generate_tests(metafunc):
    if 'start_state' in metafunc.fixturenames:
        metafunc.parametrize('start_state', ["in prog", "done", "todo"])

def test_finish(cards_db, start_state):
    index = cards_db.add_card(Card(summary="Write code", state=start_state))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"