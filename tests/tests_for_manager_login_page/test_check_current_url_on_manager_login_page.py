from data.url import Url


def test_check_current_url_on_manager_login_page(manager_login_page):
    manager_login_page.navigate()
    manager_login_page.check_current_url(Url.MANAGER_URL)