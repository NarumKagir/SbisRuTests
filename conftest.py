import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    try:
        driver.quit()
    finally:
        driver.__class__._instances = {}