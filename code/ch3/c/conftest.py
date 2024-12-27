from pathlib import Path
from tempfile import TemporaryDirectory
import cards
import pytest

@pytest.fixture(scope='session')
def db():
    """CardsDB Object conect to a temporary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()

@pytest.fixture(scope='function')
def cards_db(db):
    """CardsDB Object that's empty"""
    db.delete_all()
    return db

@pytest.fixture(scope='session')
def some_cards():
    return [
        cards.Card(summary="Write code", owner="Mark", state="done"),
        cards.Card(summary="Write code", owner="Alice", state="done"),
        cards.Card(summary="Review PR", owner="Bob", state='todo'),
        cards.Card(summary="Update documentation", owner="Carol", state='todo'),
    ]
    
@pytest.fixture(scope='function')
def non_empty_cards_db(cards_db, some_cards):
    """CardsDB Object that's been populated with 'some cards'"""
    for card in some_cards:
        cards_db.add_card(card)
    return cards_db
