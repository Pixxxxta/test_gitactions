from pages.login_page import LoginHelper


class TestLogin:
    def test_login_success(self, browser):
        login_page = LoginHelper(browser)
        login_page.load_site()
        login_page.set_email('pixta@pixta.com')
        login_page.set_password('pixta')
        login_page.click_login_btn()

        assert login_page.check_organization_name(organization_name='ИП "Виталя"'), \
            "Название организации не совпадает с ожидаемым"
