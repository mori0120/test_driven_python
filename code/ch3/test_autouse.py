import pytest
import time

@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Report the time at the end of a session"""
    yield
    now = time.time()
    print("--")
    print(f'finished: {time.strftime("%d %b %X", time.localtime(now))}')
    print('--------------------')

@pytest.fixture(autouse=True)
def footer_function_scope():
    """Report test durations after each function"""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print(f'\ntest duration: {delta:.3f} seconds')

def test_1():
    """Simulate long test"""
    time.sleep(1)

def test_2():
    """Simulate longer test"""
    time.sleep(1.3)