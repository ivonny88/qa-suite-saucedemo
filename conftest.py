import pytest
import os
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.users import STANDARD_USER


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        headless = os.getenv("CI", "false").lower() == "true"
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="function")
def logged_in_page(page):
    login = LoginPage(page)
    login.open()
    login.login(STANDARD_USER["username"], STANDARD_USER["password"])
    inventory = InventoryPage(page)
    assert inventory.is_loaded(), "Login failed — inventory page not loaded"
    yield page