import pytest
from packaging.version import parse
import cards
from cards import Card

@pytest.mark.xfail(
    parse(cards.__version__).major < 2,
    reason='Card does not support < comparison in 1.X releases.'
)
def test_less_than():
    c1 = Card(summary="a task")
    c2 = Card(summary="b task")
    assert c1 < c2

@pytest.mark.xfail(reason='xpass demo')
def test_xpass():
    c1 = Card(summary="a task")
    c2 = Card(summary="a task")
    assert c1 == c2

@pytest.mark.xfail(reason='strict demo', strict=True)
def test_xfail_strict():
    c1 = Card(summary="a task")
    c2 = Card(summary="a task")
    assert c1 == c2