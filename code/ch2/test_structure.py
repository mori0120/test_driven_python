from cards import Card

def test_to_dict():
    # Given/Arrange: 前提
    c1 = Card('something', 'brian', 'todo', 123)

    # When/Act: もし
    c2 = c1.to_dict()

    # Then/Assert: ならば
    c2_expected = {
        'summary': 'something',
        'owner': 'brian',
        'state': 'todo',
        'id': 123
    }
    assert c2 == c2_expected