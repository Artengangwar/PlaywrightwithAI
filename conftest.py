import pytest
from config.config import Config


@pytest.fixture(scope="session")
def config():
    """Return the test configuration object (simple container)."""
    return Config()

