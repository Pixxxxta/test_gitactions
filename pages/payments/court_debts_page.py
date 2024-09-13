import time

from selenium.common import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from utils.appium_helpers import AppiumHelpers


# Судебные задолженности
class CourtDebtsPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def set_fio(self, fio):
        self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View'
            '/android.view.View/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.widget.EditText[1]').send_keys(fio)

    def set_date(self, date):
        self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View'
            '/android.view.View/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.widget.EditText[2]').send_keys(date)

    def choose_region(self, region):
        self._helpers.wait_and_click(
            '//android.widget.Button[@text="Регион для проверки долгов Республика Адыгея (Адыгея)"]'
        )
        time.sleep(5)
        self._helpers.wait_for_element('//android.widget.EditText').send_keys(region[:-1])
        time.sleep(5)
        self._helpers.wait_and_click(f'//*[@text="{region}"]')

    def click_check_btn(self):
        time.sleep(5)
        self._helpers.wait_and_click('//android.widget.Button[@text="Проверить"]')

    def verify_no_arrears(self, timeout=60):
        """Проверка, что штрафов нет"""
        try:
            no_arrears_check = self._helpers.wait_for_element(
                '//*[@text="ЗAДОЛЖЕННОСТЕЙ НЕТ, ПОЗДРАВЛЯЕМ!"]',
                timeout)
            return no_arrears_check is not None
        except TimeoutException:
            return False

    def click_payment_btn(self, timeout=60):
        self._helpers.wait_and_click('//android.widget.Button[@text="Оплатить"]', timeout)

    def verify_payment_page_loaded(self, timeout=20):
        """Проверяет, что страница оплаты загружена."""
        try:
            payment_page_identifier = self._helpers.wait_for_element(
                '//android.view.View[@text="Платёжный сервис А3"]/android.view.View['
                '1]/android.view.View/android.view.View/android.view.View[2]',
                timeout)
            return payment_page_identifier is not None
        except TimeoutException:
            return False

    def check_payer_fio(self, fio='Имя Фамилия'):
        fio_input = self._helpers.wait_for_element('//android.widget.EditText')
        if fio_input.text == '-' or fio_input.text == '':
            fio_input.clear()
            fio_input.send_keys(fio)

    def click_add_document_button(self):
        """
        Функция для добавления документа, если среди сохранённых нет текущего документа для проверки
        """
        self._helpers.wait_and_click('//android.widget.Button[@text="Добавить документ"]')

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

    def check_test_payment_text(self):
        try:
            test_payment_identifier = self._helpers.is_element_present('//android.widget.TextView[@text="Тест оплаты"]')
            return test_payment_identifier is not None
        except TimeoutException:
            return False

    def check_saved_doc(self, fio):
        """
            Функция для проверки сохранённых проверок

            :param fio: ФИО

            :return: XPath найденного документа или None.
        """
        doc_xpath = f'//android.widget.TextView[@text="{fio}"]'
        if self._helpers.is_element_present(value=doc_xpath):
            return doc_xpath
        return None

    def click_saved_doc(self, value):
        self._helpers.wait_and_click(value=value)

    def add_doc(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Добавить документ"]')

    def check_add_doc_btn(self):
        return self._helpers.is_element_present(value='//android.widget.Button[@text="Добавить документ"]')