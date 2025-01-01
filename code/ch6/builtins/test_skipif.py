import pytest
from packaging.version import parse
import cards
from cards import Card

@pytest.mark.skipif(
    parse(cards.__version__).major < 2,
    reason='Card does not support < comparison in 1.X releases.'
)
def test_less_than():
    c1 = Card(summary="a task")
    c2 = Card(summary="b task")
    assert c1 < c2

def test_equality():
    c1 = Card(summary="a task")
    c2 = Card(summary="a task")
    assert c1 == c2