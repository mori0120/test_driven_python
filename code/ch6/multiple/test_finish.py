import pytest
from cards import Card, InvalidCardId

pytestmark = pytest.mark.finish

@pytest.mark.smoke
class TestFinish:
    def test_finish_from_todo(self, cards_db):
        """
        finish changes state from 'todo' to 'done'
        """
        i = cards_db.add_card(Card("foo", state="todo"))
        cards_db.finish(i)
        c = cards_db.get_card(i)
        assert c.state == "done"

    def test_finish_from_in_prog(self, cards_db):
        """
        finish changes state from 'in prog' to 'done'
        """
        i = cards_db.add_card(Card("foo", state="in prog"))
        cards_db.finish(i)
        c = cards_db.get_card(i)
        assert c.state == "done"

    def test_finish_from_done(self, cards_db):
        """
        finish changes state from 'done' to 'done'
        """
        i = cards_db.add_card(Card("foo", state="done"))
        cards_db.finish(i)
        c = cards_db.get_card(i)
        assert c.state == "done"


@pytest.mark.parametrize(
    "start_state",
    [
        "todo",
        pytest.param("in prog", marks=pytest.mark.smoke),
        "done",
    ]
)
def test_finish_func(cards_db, start_state):
    """
    finish changes state from any state to 'done'
    """
    i = cards_db.add_card(Card("foo", state=start_state))
    cards_db.finish(i)
    c = cards_db.get_card(i)
    assert c.state == "done"


@pytest.fixture(
    params=[
        "todo",
        pytest.param("in prog", marks=pytest.mark.smoke),
        "done",
    ]

)
def start_state_fixture(request):
    return request.param

def test_finish_fix(cards_db, start_state_fixture):
    """
    finish changes state from any state to 'done'
    """
    i = cards_db.add_card(Card("foo", state=start_state_fixture))
    cards_db.finish(i)
    c = cards_db.get_card(i)
    assert c.state == "done"


@pytest.mark.smoke
@pytest.mark.exception
def test_finish_non_exist(cards_db):
    """
    Shouldn't be able to finish a non-existent card
    """
    any_number = 123
    with pytest.raises(InvalidCardId):
        cards_db.finish(any_number)