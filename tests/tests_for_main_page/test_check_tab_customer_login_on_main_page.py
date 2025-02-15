def test_check_tab_customer_login_on_main_page(main_page):
    main_page.navigate()
    main_page.check_element_visibility(main_page.tab_customer_login)