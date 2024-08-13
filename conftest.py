# File contains necessary pytest fixtures

import pytest
from utils.webdriver_setup import get_driver


@pytest.fixture
def driver():
    """Open and close browser"""
    driver = get_driver()
    yield driver
    driver.quit()
