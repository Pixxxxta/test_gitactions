from selenium.common import TimeoutException
from utils.appium_helpers import AppiumHelpers


# Страница с аккаунтом
class AccountPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def set_email(self, email):
        email_input = self._helpers.wait_for_element('//android.widget.EditText')
        email_input.send_keys(email)

    def click_send_email_btn(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Отправить"]')

    def go_to_payment_history(self):
        self._helpers.find_element_with_scroll('//android.widget.TextView[@text="История платежей"]')

    def go_to_saved_cards(self):
        self._helpers.find_element_with_scroll('//android.widget.TextView[@text="Сохраненные карты"]')

    def go_to_language(self):
        self._helpers.find_element_with_scroll('//android.widget.TextView[@text="Язык"]')

    def go_to_saved_docs(self, doc_type):
        """
        Функция для ввода серии и номера патента в одно поле

        :param doc_type: Тип сохранённого документа
                - Паспорта (не РФ)
                - Автомобили
                - Водительские удостоверения
                - Патенты
                - ИНН
                - Вид на жительство
                - Разрешение на временное проживание
        """
        element = self._helpers.find_element_with_scroll(f'//android.view.View[@text="{doc_type}"]')
        element.click()

    def click_saved_doc(self, doc_type, doc_num):
        """
        Функция для ввода серии и номера патента в одно поле

        :param doc_num: Номер документа
            Для автомобильного номера указывать регион вместе с номером - А123ВВ102
        :param doc_type: Тип сохранённого документа
                - Паспорт
                - Госномер
                - Водительские удостоверения
                - Патент
                - ИНН
                - Вид на жительство
                - Разрешение на временное проживание
        """
        self._helpers.wait_and_click(f'//android.widget.TextView[@text="{doc_type} {doc_num}"]')



