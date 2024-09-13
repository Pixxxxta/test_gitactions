from selenium.common import TimeoutException
from utils.appium_helpers import AppiumHelpers


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

        patent_input = self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view.View'
            '/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]')

        date_of_issue_input = self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view.View'
            '/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]')

        last_name_input = self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view.View'
            '/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[3]')

        name_input = self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view.View'
            '/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[4]')

        passport_input = self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view.View'
            '/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[5]')

        inn_input = self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view.View'
            '/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[6]')

        patent_input.send_keys(series_number)
        date_of_issue_input.send_keys(date_of_issue_patent)
        last_name_input.send_keys(last_name)
        name_input.send_keys(name)
        passport_input.send_keys(passport)
        inn_input.send_keys(inn)

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

    def verify_payment_page_loaded(self, timeout=20):
        """Проверяет, что страница оплаты загружена."""
        try:
            payment_page_identifier = self._helpers.wait_for_element('//android.view.View[@text="ОПЛАТА"]',
                                                                     timeout=timeout)
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

