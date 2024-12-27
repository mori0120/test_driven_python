import pytest

@pytest.fixture(name='renamed_fixture')
def not_renamed_fixture():
    return 'fixture'

def test_rename_fixture(renamed_fixture):
    assert renamed_fixture == 'fixture'