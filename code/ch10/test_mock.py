from unittest import mock

import cards
import pytest
from cards.cli import app
from typer.testing import CliRunner

runner = CliRunner()

def test_mock_version():
    with mock.patch.object(cards, "__version__", "1.2.3"):
        result = runner.invoke(app, ["version"])
        assert result.stdout.rstrip() == "1.2.3"

def test_mock_CardsDB():
    with mock.patch.object(cards, "CardsDB") as MockCardsDB:
        print()
        print(f"       class:{MockCardsDB}")
        print(f"return_value:{MockCardsDB.return_value}")
        with cards.cli.cards_db() as db:
            print(f"      object:{db}")

def test_mock_path():
    with mock.patch.object(cards, "CardsDB") as MockCardsDB:
        MockCardsDB.return_value.path.return_value = "/foo/"
        with cards.cli.cards_db() as db:
            print()
            print(f"{db.path=}")
            print(f"{db.path()=}")

@pytest.fixture()
def mock_cardsdb():
    with mock.patch.object(cards, "CardsDB", autospec=True) as CardsDB:
        yield CardsDB.return_value

def test_config(mock_cardsdb):
    mock_cardsdb.path.return_value = "/foo/"
    result = runner.invoke(app, ["config"])
    assert result.stdout.rstrip() == "/foo/"

def test_bad_mock():
    with mock.patch.object(cards, "CardsDB") as MockCardsDB:
        db = MockCardsDB("/some/path")
        db.path()
        db.path(35)
        db.not_valid()

@pytest.mark.xfail(reason="test mock autospec", strict=True)
def test_good_mock():
    with mock.patch.object(cards, "CardsDB", autospec=True) as CardsDB:
        db = CardsDB("/some/path")
        db.path()
        db.path(35)
        db.not_valid()