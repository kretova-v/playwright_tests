import time


def test_check_select_option(customer_login_page):
    customer_login_page.navigate()
    customer_login_page.your_name_field.click()
    customer_login_page.select_option_1.click(force=True)
