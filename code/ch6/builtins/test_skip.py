import pytest
from cards import Card

@pytest.mark.skip(reason='Card does not support < comparison yet.')
def test_less_than():
    c1 = Card(summary="a task")
    c2 = Card(summary="b task")
    assert c1 < c2

def test_equality():
    c1 = Card(summary="a task")
    c2 = Card(summary="a task")
    assert c1 == c2