from pages.services.payments.patent_page import PatentPage
from pages.start_page import StartPage
from pages.services.payments.payments_page import PaymentsPage
from pages.services.services_page import ServicesPage
import time
import allure
import pytest
from utils.screenshot_helper import take_screenshot


class TestPaymentPatent:

    @allure.feature('Проверка оплаты патента')
    @pytest.mark.parametrize("series_number, last_name, name, inn, passport, date_of_issue_patent", [
        ('772204315436', 'АБДУРОСУЛОВ', 'ДОСТОН', '971510764678', 'FA6169953', '01012020')
    ])
    @pytest.mark.group1
    def test_payment_patent(self, appium_driver, series_number, last_name, name, inn, passport, date_of_issue_patent):
        start_page = StartPage(appium_driver)
        patent_page = PatentPage(appium_driver)
        services_page = ServicesPage(appium_driver)
        take_screenshot(driver=appium_driver, test_name='test_payment_patent',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_launch_app")

        start_page.go_to_services()
        take_screenshot(driver=appium_driver, test_name='test_payment_patent',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_go_to_services")
        services_page.go_to_payment_patent()
        take_screenshot(driver=appium_driver, test_name='test_payment_patent',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_go_to_payment_patent")
        # if not patent_page.check_saved_patent(series_number):
        #     patent_page.click_add_patent()
        time.sleep(40)
        take_screenshot(driver=appium_driver, test_name='test_payment_patent',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_sleep_40")
        patent_page.set_patent_series_number(series_number, last_name, name, inn, passport, date_of_issue_patent)
        take_screenshot(driver=appium_driver, test_name='test_payment_patent',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_input_data")

        patent_page.scroll_down()
        time.sleep(1)
        patent_page.scroll_down()
        time.sleep(1)
        patent_page.click_payment_button()
        take_screenshot(driver=appium_driver, test_name='test_payment_patent',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_click_payment_btn")

        # Проверка на наличие загрузку страницы оплаты
        assert patent_page.verify_payment_page_loaded(), \
            f'На странице не появилась форма для оплаты - {series_number}, {last_name}, {name}, {inn}, {passport}, {date_of_issue_patent}'
        take_screenshot(driver=appium_driver, test_name='test_payment_patent',
                        folder_name='payments_page',
                        screenshot_name=f"screen_verify_payment_page_loaded")

        # # Проверка на наличие текста "Тест оплаты"
        # assert patent_page.check_test_payment_text(), 'На странице не появился текст для тестовой оплаты'
        #
        # # Кнопка оплаты
        # patent_page.click_success_payment_btn()
        # time.sleep(1)
        #
        # # Проверка на наличие текста "ОПЛАТА УСПЕШНО ПРОИЗВЕДЕНА!"
        # assert patent_page.verify_payment_success(), 'Произошла ошибка при оплате'
        start_page.reset_user()

    @allure.feature('Проверка оплаты патента с неправильным форматом ИНН')
    @pytest.mark.parametrize("series_number, last_name, name, inn, passport, date_of_issue_patent", [
        ('772204315436', 'АБДУРОСУЛОВ', 'ДОСТОН', '971510764677', 'FA6169953', '01.01.2020')
    ])
    @pytest.mark.group4
    def test_payment_patent_with_wrong_inn(self, appium_driver, series_number, last_name, name, inn, passport, date_of_issue_patent):
        start_page = StartPage(appium_driver)
        patent_page = PatentPage(appium_driver)
        services_page = ServicesPage(appium_driver)
        take_screenshot(driver=appium_driver, test_name='test_payment_patent_with_wrong_inn',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_launch_app")

        start_page.go_to_services()
        services_page.go_to_payment_patent()

        patent_page.set_patent_series_number(series_number, last_name, name, inn, passport, date_of_issue_patent)
        take_screenshot(driver=appium_driver, test_name='test_payment_patent_with_wrong_inn',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_input_data")

        patent_page.scroll_down()
        time.sleep(1)
        patent_page.click_payment_button()
        take_screenshot(driver=appium_driver, test_name='test_payment_patent_with_wrong_inn',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_click_payment_btn")

        # Проверка на наличие загрузку страницы оплаты
        assert patent_page.verify_inn_error(), \
            f'На не появилось сообщение об ошибке формата ИНН - {series_number}, {last_name}, {name}, {inn}, {passport}, {date_of_issue_patent}'
        take_screenshot(driver=appium_driver, test_name='test_payment_patent_with_wrong_inn',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_verify_inn_error")
