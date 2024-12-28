from cards import Card

def test_finish(cards_db):
    for c in [
        Card(summary="Write code", state="in prog"),
        Card(summary="Write code2", state="done"),
        Card(summary="Write code3", state="todo"),
    ]:
        index = cards_db.add_card(c)
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == "done"