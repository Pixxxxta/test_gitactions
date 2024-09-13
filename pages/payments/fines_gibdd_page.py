from selenium.common import TimeoutException
from utils.appium_helpers import AppiumHelpers


# Штрафы ГИБДД
class GIBDDPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def choose_doc_type(self, doc_type='Паспорт иностранного гражданина'):
        """
        Функция для выбора типа документа

        :param doc_type: Выбор типа документа проверки:
            - Автомобиль (стоит по умолчанию)
            - Водитель
            - УИН
        """
        self._helpers.wait_and_click(f'//android.view.View[@text="{doc_type}"]')

    def set_car_number(self, doc_number, region):
        self._helpers.wait_for_element(
            '//android.widget.EditText[@resource-id="sp-input-0"]').send_keys(
            doc_number)
        self._helpers.wait_for_element(
            '//android.widget.EditText[@resource-id="sp-input-1"]').send_keys(
            region)

    def set_driver_number(self, doc_number):
        self._helpers.wait_for_element('//android.widget.EditText').send_keys(doc_number)

    def set_UIN_number(self, uin):
        self._helpers.wait_for_element('//android.widget.EditText').send_keys(uin)

    def click_check_btn(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Проверить"]')

    def click_payment_btn(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Оплатить"]')

    def verify_no_fines(self, timeout=60):
        """Проверка, что штрафов нет"""
        try:
            no_fines_check = self._helpers.wait_for_element('//*[@text="ШТРАФОВ НЕТ, ПОЗДРАВЛЯЕМ!"]', timeout)
            return no_fines_check is not None
        except TimeoutException:
            return False

    def verify_have_fines(self, timeout=20):
        """Проверка, что штрафы есть"""
        try:
            fines_check = self._helpers.wait_for_element('//android.widget.Button[@text="Оплатить"]', timeout)
            return fines_check is not None
        except TimeoutException:
            return False

    def go_to_payment(self):
        # TODO Добавить выбор штрафов
        self._helpers.wait_and_click('//android.widget.Button[@text="Оплатить"]')

    def verify_payment_page_loaded(self, timeout=20):
        """Проверяет, что страница оплаты загружена."""
        try:
            payment_page_identifier = self._helpers.wait_for_element('//android.view.View[@text="ОПЛАТА"]',
                                                                     timeout=timeout)
            return payment_page_identifier is not None
        except TimeoutException:
            return False

    def check_payer_fio(self, fio='Имя Фамилия'):
        fio_input = self._helpers.wait_for_element('//android.widget.EditText')
        if fio_input.text == '-' or fio_input.text == '':
            fio_input.clear()
            fio_input.send_keys(fio)

    def check_saved_doc(self, doc_number,doc_category, region=None):
        """
            Функция для проверки сохранённых проверок

            :param doc_number: Номер документа
            :param region: Регион для автомобильного номера

            :param doc_category: Выбор категории:
                - Госномер
                - Водительское удостоверение

            :return: XPath найденного документа или None.
        """
        if region is not None:
            doc_xpath = f'//android.widget.TextView[@text="{doc_category} {doc_number}{region}"]'
        else:
            doc_xpath = f'//android.widget.TextView[@text="{doc_category} {doc_number}"]'
        if self._helpers.is_element_present(value=doc_xpath):
            return doc_xpath
        return None

    def click_saved_doc(self, value):
        self._helpers.wait_and_click(value=value)

    def add_doc(self):
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
