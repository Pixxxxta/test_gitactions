from selenium.common import TimeoutException
from utils.appium_helpers import AppiumHelpers


# Штрафы МВД
class MVDPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def set_data(self, doc_category='Паспорт иностранного гражданина', doc_number='FA6169953'):
        """
        Функция для заполнения данных

        :param doc_number: Номер документа

        :param doc_category: Выбор категории:
            - Паспорт иностранного гражданина (стоит по умолчанию)
            - Вид на жительство в Российской Федерации
            - Разрешение на временное проживание в Российской Федерации
        """

        try:
            if doc_category != 'Паспорт иностранного гражданина':
                # Открываем выпадающий список категории документа
                self._helpers.wait_and_click('//android.view.View[@text="Паспорт иностранного гражданина"]')
                # Выбираем категорию документа
                self._helpers.wait_and_click(
                    f'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="{doc_category}"]')

            # Вводим номер документа
            self._helpers.wait_and_click('//android.widget.EditText')
            self._helpers.adb_input_text(doc_number)
            self._helpers.click_back_btn()

        except TimeoutException:
            print("Элемент не найден или не кликабелен в течение заданного времени.")

    def click_check_btn(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Проверить"]')

    def add_doc(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Добавить документ"]')

    def verify_no_fines(self, timeout=60):
        """Проверка, что штрафов нет"""
        try:
            no_fines_check = self._helpers.wait_for_element('//*[@text="ШТРАФОВ НЕТ, ПОЗДРАВЛЯЕМ!"]', timeout)
            return no_fines_check is not None
        except TimeoutException:
            return False

    def verify_have_fines(self, timeout=60):
        """Проверка, что штрафы есть"""
        try:
            fines_check = self._helpers.wait_for_element('//android.widget.Button[@text="Оплатить"]', timeout)
            return fines_check is not None
        except TimeoutException:
            return False

    def check_payer_fio(self, fio='Имя Фамилия'):
        fio_input = self._helpers.wait_for_element('//android.widget.EditText')
        if fio_input.text == '-' or fio_input.text == '':
            fio_input.clear()
            fio_input.send_keys(fio)

    def click_payment_btn(self, timeout=60):
        self._helpers.wait_and_click('//android.widget.Button[@text="Оплатить"]', timeout)

    def verify_payment_page_loaded(self, timeout=60):
        """Проверяет, что страница оплаты загружена."""
        try:
            payment_page_identifier = self._helpers.wait_for_element(
                '//android.view.View[@text="Платёжный сервис А3"]/android.view.View['
                '1]/android.view.View/android.view.View/android.view.View[2]', timeout)
            return payment_page_identifier is not None
        except TimeoutException:
            return False

    def check_saved_doc(self, doc_number, doc_category):
        """
            Функция для проверки сохранённых документов

            :param doc_number: Номер документа

            :param doc_category: Выбор категории:
                - Паспорт
                - Вид на жительство
                - Разрешение на временное проживание

            :return: XPath найденного документа или None.
        """
        doc_xpath = f'//android.widget.TextView[@text="{doc_category} {doc_number}"]'
        if self._helpers.is_element_present(value=doc_xpath, timeout=5):
            return doc_xpath
        return None

    def click_saved_doc(self, value):
        self._helpers.wait_and_click(value=value, timeout=5)

    def check_add_doc_btn(self):
        return self._helpers.is_element_present(value='//android.widget.Button[@text="Добавить документ"]', timeout=5)

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