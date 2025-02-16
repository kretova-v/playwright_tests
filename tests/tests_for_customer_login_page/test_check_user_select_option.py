import time


def test_check_select_option(customer_login_page):
    customer_login_page.navigate()
    customer_login_page.your_name_field.click()

