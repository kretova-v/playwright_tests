
def test_check_button_home_on_main_page(main_page):
    main_page.navigate()
    main_page.check_element_visibility(main_page.tab_home)
