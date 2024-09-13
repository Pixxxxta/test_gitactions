import time

from selenium.common import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from utils.appium_helpers import AppiumHelpers
import os


# Оплата налогов
class TaxesPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def choose_doc_type(self, doc_type):
        self._helpers.wait_and_click(f'(//android.view.View[@text="{doc_type}"])')
        time.sleep(5)
        screenshot_path = os.path.abspath(os.path.join(os.getcwd(), 'artifacts', 'screenshot_choose_doc_type.png'))
        self._driver.save_screenshot(screenshot_path)

    def set_document_data(self, doc_num):
        """
        Функция для выбора типа документа проверки и вставки значения
        :param doc_num: Номер документа
        """
        self._helpers.wait_for_element('//android.widget.EditText').send_keys(doc_num)
        time.sleep(5)
        screenshot_path = os.path.abspath(os.path.join(os.getcwd(), 'artifacts', 'screenshot_set_doc_data.png'))
        self._driver.save_screenshot(screenshot_path)

    def click_check_btn(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Проверить"]')
        time.sleep(5)
        screenshot_path = os.path.abspath(os.path.join(os.getcwd(), 'artifacts', 'screenshot_click_check_btn.png'))
        self._driver.save_screenshot(screenshot_path)

    def verify_no_arrears(self, timeout=20):
        """Проверка, что штрафов нет"""
        screenshot_path = os.path.abspath(os.path.join(os.getcwd(), 'artifacts', 'screenshot_verify_no_arrears.png'))
        self._driver.save_screenshot(screenshot_path)
        try:
            no_arrears_check = self._helpers.wait_for_element(
                '//*[@text="ЗAДОЛЖЕННОСТЕЙ НЕТ, ПОЗДРАВЛЯЕМ!"]',
                timeout)
            return no_arrears_check is not None
        except TimeoutException:
            return False

    def click_payment_btn(self, timeout=20):
        self._helpers.wait_and_click('//android.widget.Button[@text="Оплатить"]', timeout)

    def verify_payment_page_loaded(self, timeout=20):
        """Проверяет, что страница оплаты загружена."""
        try:
            payment_page_identifier = self._helpers.wait_for_element('//android.view.View[@text="ОПЛАТА"]',
                                                                     timeout=timeout)
            return payment_page_identifier is not None
        except TimeoutException:
            return False

    def check_payer_fio(self, fio='Имя Фамилия'):
        time.sleep(1)
        fio_input = self._helpers.wait_for_element('//android.widget.EditText')
        if fio_input.text == '-' or fio_input.text == '':
            fio_input.clear()
            fio_input.send_keys(fio)

    def check_saved_doc(self, doc_num, doc_type='ИНН'):
        """
        Функция для проверки наличия сохранённого документа
        :param doc_num: Номер документа
        :param doc_type:
            - ИНН (стоит по умолчанию)
            - УИН
        :return: объект, если найден, иначе False
        """

        doc_xpath = f'//android.widget.TextView[@text="{doc_type} {doc_num}"]'
        if self._helpers.is_element_present(value=doc_xpath):
            return doc_xpath
        return None

    def click_saved_doc(self, value):
        self._helpers.wait_and_click(value=value)

    def click_add_document_button(self):
        """
        Функция для добавления документа, если среди сохранённых нет текущего документа для проверки
        """
        self._helpers.wait_and_click('//android.widget.Button[@text="Добавить документ"]')

    def check_add_doc_btn(self):
        return self._helpers.is_element_present(value='//android.widget.Button[@text="Добавить документ"]')

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
