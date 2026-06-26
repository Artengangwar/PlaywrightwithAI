import pytest
from config.config import Config


# The pytest-playwright plugin provides these fixtures automatically:
# - page: A single page instance for each test
# - browser: A browser instance
# - context: A browser context
#
# You don't need to define them here - they come from the pytest-playwright plugin.
# To run with these fixtures, use: pytest tests/


@pytest.fixture(scope="session")
def config():
    """Return the test configuration object (simple container)."""
    return Config()

