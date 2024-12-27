def test_add_some(cards_db, some_cards):
    expected = len(some_cards)
    for c in some_cards:
        cards_db.add_card(c)
    assert cards_db.count() == expected

def test_non_empty(non_empty_cards_db):
    assert non_empty_cards_db.count() > 0