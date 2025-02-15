from playwright.sync_api import Page
from select import select

from data.url import Url
from page_objects.base_page import BasePage


class CustomerLoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.button = None
        self.page = page
        self.your_name_field = page.locator("#userSelect")
        self.select_option_1 = page.get_by_test_id('cust in Customers').nth(1)
        self.select_option_2 = page.locator("#userSelect")
        self.select_option_3 = page.locator("#userSelect")
        self.select_option_4 = page.locator("#userSelect")
        self.select_option_5 = page.locator("#userSelect")
        self.button_login = page.get_by_role("button", name="Login")



    def navigate(self):
        self.page.goto(Url.CUSTOMER_URL, timeout=50000)

