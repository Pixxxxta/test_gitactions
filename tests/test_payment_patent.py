from pages.services.payments.patent_page import PatentPage
from pages.start_page import StartPage
from pages.services.payments.payments_page import PaymentsPage
import time
import allure
import pytest


class TestPaymentPatent:
    @allure.feature('Проверка оплаты патента')
    @pytest.mark.parametrize("series_number, last_name, name, inn, passport, date_of_issue_patent", [
        ('77 2204315436', 'АБДУРОСУЛОВ', 'ДОСТОН', '971510764678', 'FA6169953', '01.01.2020')
    ])
    def test_payment_patent(self, appium_driver, series_number, last_name, name, inn, passport, date_of_issue_patent):
        start_page = StartPage(appium_driver)
        patent_page = PatentPage(appium_driver)
        payments_page = PaymentsPage(appium_driver)

        start_page.go_to_payments()
        payments_page.go_to_payment_patent()
        if not patent_page.check_saved_patent(series_number):
            patent_page.click_add_patent()
            patent_page.set_patent_series_number(series_number, last_name, name, inn, passport, date_of_issue_patent)

        patent_page.scroll_down()
        time.sleep(1)
        patent_page.click_payment_button()

        # Проверяется, произошёл ли переход на страницу с оплатой
        assert patent_page.verify_payment_page_loaded(), 'Не удалось перейти на страницу оплаты'
