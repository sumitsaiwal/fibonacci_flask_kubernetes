import pytest
from app.app import app

@pytest.fixture
def client():
    """A test client for the app."""
    yield app.test_client()
    ## Below can be the teardown of client after each test
    