import time

from selenium.common import TimeoutException
from utils.appium_helpers import AppiumHelpers
from utils.screenshot_helper import take_screenshot



# Оплата патента
class PatentPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def set_patent_series_number(self, series_number, last_name, name, inn, passport, date_of_issue_patent):
        """
        Функция для ввода серии и номера патента в одно поле

        :param date_of_issue_patent: Дата выдачи патента
        :param passport: Серия и номер паспорта
        :param inn: ИНН
        :param name: Имя
        :param last_name: Фамилия
        :param series_number: Серия и номер патента
        """
        self.scroll_down()
        take_screenshot(driver=self._driver, test_name='test_payment_patent',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_scroll_down")
        elements = self._helpers.find_all_edittexts()
        elements[0].click()
        self._helpers.adb_input_text(series_number)
        self._driver.hide_keyboard()
        elements[1].click()
        self._helpers.adb_input_text(date_of_issue_patent)
        self._driver.hide_keyboard()
        elements[2].send_keys(last_name)
        elements[3].send_keys(name)
        elements[4].click()
        self._helpers.adb_input_text(passport)
        self._driver.hide_keyboard()
        elements[5].click()
        self._helpers.adb_input_text(inn)
        self._driver.hide_keyboard()

    def swipe_down_to_button(self):
        self._helpers.swipe_down()

    def scroll_down(self):
        self._helpers.swipe_down()

    def back_to_payments_page(self):
        self._driver.press_keycode(4)
        self._driver.press_keycode(4)
        self._driver.press_keycode(4)

    def click_payment_button(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Оплатить"]')

    def click_add_patent(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Добавить патент"]')

    def pick_payment_count_months(self, count=1):
        for i in range(count):
            self._helpers.wait_and_click(
                '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view.View'
                '/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View['
                '5]/android.view.View[3]')

    def verify_payment_page_loaded(self, timeout=60):
        """Проверяет, что страница оплаты загружена."""
        try:
            payment_page_identifier = self._helpers.wait_for_element(
                '//android.view.View[@text="Платёжный сервис А3"]/android.view.View['
                '1]/android.view.View/android.view.View/android.view.View[2]', timeout)
            return payment_page_identifier is not None
        except TimeoutException:
            return False

    def check_saved_patent(self, patent_num):
        patent_num = patent_num.replace(' ', '')
        try:
            self._helpers.wait_and_click(f'//android.widget.TextView[@text="Патент {patent_num}"]')
            return True
        except TimeoutException:
            return False

    def check_test_payment_text(self):
        try:
            test_payment_identifier = self._helpers.is_element_present('//android.widget.TextView[@text="Тест оплаты"]')
            return test_payment_identifier is not None
        except TimeoutException:
            return False

    def click_success_payment_btn(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="success"]')

    def click_fail_payment_btn(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="fail"]')

    def verify_payment_success(self):
        try:
            test_success_payment_identifier = self._helpers.is_element_present('//android.widget.TextView['
                                                                               '@text="ОПЛАТА УСПЕШНО ПРОИЗВЕДЕНА!"]')
            return test_success_payment_identifier is not None
        except TimeoutException:
            return False

    def verify_inn_error(self):
        try:
            inn_error_identifier = self._helpers.is_element_present('//*[@text="ИНН: недопустимый формат"]')
            return inn_error_identifier is not None
        except TimeoutException:
            return False

