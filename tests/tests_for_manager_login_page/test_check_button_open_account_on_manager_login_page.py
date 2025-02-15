def test_check_button_open_account_on_manager_login_page(manager_login_page):
    manager_login_page.navigate()
    manager_login_page.check_element_visibility(manager_login_page.button_open_account)