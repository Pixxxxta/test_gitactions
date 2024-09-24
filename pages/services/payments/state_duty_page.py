import time

from selenium.common import TimeoutException
from utils.appium_helpers import AppiumHelpers


# Оплата госпошлины
class StateDutyPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def choose_duty_category(self, duty_category='За выдачу паспорта гражданина Российской Федерации'):
        self._helpers.wait_and_click('(//*[@text="Выберите"])')
        time.sleep(5)
        # Выбираем категорию пошлины
        self._helpers.wait_and_click(f'//*[@text="{duty_category}"]')

    def choose_city(self, city='Москва'):
        time.sleep(2)
        self._helpers.wait_and_click('//*[@text="Выберите"]')
        time.sleep(5)
        self._helpers.wait_and_click(f'//*[@text="{city}"]')

    def set_doc_num(self, doc_num):
        elements = self._helpers.find_all_edittexts()
        print(elements)
        elements[0].send_keys(doc_num)

    def set_fio(self, fio):
        elements = self._helpers.find_all_edittexts()
        print(elements)
        elements[1].send_keys(fio)

    def click_payment_btn(self):
        time.sleep(3)
        self._helpers.wait_and_click('//android.widget.Button[@text="Оплатить"]')

    def set_data(self, duty_category='За выдачу паспорта гражданина Российской Федерации', city='Москва',
                 document='Паспорт иностранного гражданина', fio='АБДУРОСУЛОВ ДОСТОН', doc_number='FA6169953',
                 inn='7701107259', payment_account='03100643000000017300', bik='004525988', oktmo='45375000'):
        """
        Функция для заполнения данных

        :param oktmo: ОКТМО
        :param bik: БИК
        :param payment_account: Р/С получается
        :param inn: ИНН получателя
        :param doc_number: Номер документа
        :param fio: Фамилия Имя Отчество(при наличии)
        :param document: Выбор документа, удостоверяющего личность
            - Паспорт иностранного гражданина (стоит по умолчанию)
            - Вид на жительство в Российской Федерации
            - Разрешение на временное проживание в Российской Федерации

        :param duty_category: Выбор категории:
            - За выдачу паспорта гражданина Российской Федерации (ставится по умолчанию)
            - За выдачу вида на жительство иностранному гражданину или лицу без гражданства
            - За прием в гражданство РФ
            - За выдачу иностранному гражданину или лицу без гражданства разрешения на временное проживание в РФ

        :param city: Выбор категории:
            - Москва (ставится по умолчанию)
            - Казань
            - Санкт-Петербург
            - Нижний новгород
            - Самара
            - Другой
        """

        try:
            # Открываем выпадающий список категории пошлины
            self._helpers.wait_and_click('(//android.view.View[@text="Выберите"])[1]')
            # Выбираем категорию пошлины
            self._helpers.wait_and_click(
                f'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="{duty_category}"]')

            # Открываем выпадающий список города
            self._helpers.wait_and_click('(//android.view.View[@text="Выберите"])')
            # Выбираем город
            self._helpers.wait_and_click(f'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="{city}"]')

            if city == 'Другой':
                # Вводим ИНН получателя
                inn_input = self._helpers.wait_for_element(
                    '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view'
                    '.View/android.view.View/android.view.View['
                    '2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')
                inn_input.send_keys(inn)

                # Вводим Р/С получателя
                payment_account_input = self._helpers.wait_for_element(
                    '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view'
                    '.View/android.view.View/android.view.View['
                    '2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
                payment_account_input.send_keys(payment_account)

                # Вводим БИК банка получается
                bik_input = self._helpers.wait_for_element(
                    '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view'
                    '.View/android.view.View/android.view.View['
                    '2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]')
                bik_input.send_keys(bik)

                # Вводим ОКТМО получателя
                oktmo_input = self._helpers.wait_for_element(
                    '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view'
                    '.View/android.view.View/android.view.View['
                    '2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[4]')
                oktmo_input.send_keys(oktmo)

            # Скролим вниз
            self._helpers.swipe_down()

            # Выбираем тип документа
            self._helpers.wait_and_click('//android.view.View[@text="Паспорт иностранного гражданина"]')
            self._helpers.wait_and_click(
                f'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="{document}"]')

            # Вводим номер документа
            document_number_input = self._helpers.wait_for_element(
                '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view.View'
                '/android.view.View/android.view.View[2]/android.view.View/android.view.View['
                '1]/android.widget.EditText[1]')
            document_number_input.send_keys(doc_number)

            # Вводим ФИО
            fio_input = self._helpers.wait_for_element(
                '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view.View'
                '/android.view.View/android.view.View[2]/android.view.View/android.view.View['
                '1]/android.widget.EditText[2]')
            fio_input.send_keys(fio)

            # Нажимаем кнопку "Оплатить"
            self._helpers.wait_and_click('//android.widget.Button[@text="Оплатить"]')

        except TimeoutException:
            print("Элемент не найден или не кликабелен в течение заданного времени.")

    def verify_payment_page_loaded_a3(self, timeout=20):
        """Проверяет, что страница оплаты загружена."""
        try:
            payment_page_identifier = self._helpers.wait_for_element(
                '//android.view.View[@text="Платёжный сервис А3"]/android.view.View['
                '1]/android.view.View/android.view.View/android.view.View[2]', timeout)
            return payment_page_identifier is not None
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
