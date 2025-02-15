from playwright.sync_api import Page, Locator, expect

from page_objects.base_page import BasePage


class ManagerLoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.button_add_customers = page.get_by_role("button", name="Add Customer")
        self.button_open_account = page.get_by_role("button", name="Open Account")
        self.button_customers = page.get_by_role("button", name="Customers")


    def navigate(self):
        self.page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager", timeout=50000)

