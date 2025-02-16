import pytest
from playwright.sync_api import Playwright

from page_objects.customer_login_page import CustomerLoginPage
from page_objects.main_page import MainPage
from page_objects.manager_login_page import ManagerLoginPage


@pytest.fixture(scope="function")
def browser(playwright: Playwright):
    playwright.selectors.set_test_id_attribute('ng-repeat')
    browser = playwright.chromium.launch(headless=False)
    return browser

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    return page

@pytest.fixture(scope="function")
def main_page(page):
    return MainPage(page)

@pytest.fixture(scope="function")
def manager_login_page(page):
    return ManagerLoginPage(page)

@pytest.fixture(scope="function")
def customer_login_page(page):
    return CustomerLoginPage(page)

