from app.app import _fibonacci

def test_fibonacci():
    """test the returned fibonacci value"""
    assert _fibonacci(42)[0] == 267914296
