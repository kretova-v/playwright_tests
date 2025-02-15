from data.url import Url


def test_check_current_url_on_customer_login_page(customer_login_page):
    customer_login_page.navigate()
    customer_login_page.check_current_url(Url.CUSTOMER_URL)
