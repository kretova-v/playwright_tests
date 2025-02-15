

from playwright.sync_api import Page, expect, Locator

from page_objects.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.top_window = page.get_by_text("Home XYZ Bank Logout")
        self.top_title = page.get_by_text("XYZ Bank")
        self.tab_home = page.get_by_role("button", name="Home")
        self.lower_window = page.get_by_text("Customer Login Bank Manager")
        self.tab_customer_login = page.get_by_role("button", name="Customer Login")
        self.tab_bank_manager_login = page.get_by_role("button", name="Bank Manager Login")



    def navigate(self):
        self.page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login", timeout=50000)














