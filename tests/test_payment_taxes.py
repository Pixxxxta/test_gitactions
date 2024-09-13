import time
import allure
from pages.payments.payment_taxes_page import TaxesPage
from pages.start_page import StartPage
from pages.payments.payments_page import PaymentsPage
import pytest


class TestTaxes:
    @pytest.mark.parametrize("doc_type, doc_num", [
        ('ИНН', '780204893183')
    ])
    @allure.feature('Проверка оплаты налогов')
    @allure.story('Проверка по ИНН без штрафов')
    def test_payment_taxes_page_inn_no_arrears(self, appium_driver, doc_type, doc_num):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных оплаты налогов
        taxes_page = TaxesPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в оплату налогов
        payments_page.go_to_payment_taxes()
        # Проверка на наличие сохранённых документов
        saved_doc = taxes_page.check_saved_doc(doc_type=doc_type, doc_num=doc_num)
        if saved_doc:
            taxes_page.click_saved_doc(value=saved_doc)
        else:
            if taxes_page.check_add_doc_btn():
                # Добавляем документ
                taxes_page.click_add_document_button()
            # Выбор типа документа проверки
            taxes_page.choose_doc_type(doc_type)
            # Ввод данных для проверки
            taxes_page.set_document_data(doc_num=doc_num)
            # Кнопка проверки
            taxes_page.click_check_btn()

        assert taxes_page.verify_no_arrears(), 'Ошибка при поиске задолженностей'

    @pytest.mark.parametrize("doc_type, doc_num, payer_fio", [
        ('ИНН', '540363052918', 'Антонио Бандерас')
    ])
    @allure.feature('Проверка оплаты налогов')
    @allure.story('Проверка по ИНН со штрафами')
    def test_payment_taxes_page_inn_have_arrears(self, appium_driver, doc_type, doc_num, payer_fio):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных оплаты налогов
        taxes_page = TaxesPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в оплату налогов
        payments_page.go_to_payment_taxes()
        # Проверка на наличие сохранённых документов
        saved_doc = taxes_page.check_saved_doc(doc_type=doc_type, doc_num=doc_num)
        if saved_doc:
            taxes_page.click_saved_doc(value=saved_doc)
        else:
            if taxes_page.check_add_doc_btn():
                # Добавляем документ
                taxes_page.click_add_document_button()
            # Выбор типа документа проверки
            taxes_page.choose_doc_type(doc_type)
            # Ввод данных для проверки
            taxes_page.set_document_data(doc_num=doc_num)
            # Кнопка проверки
            taxes_page.click_check_btn()
        # Заполнение фио плательщика
        taxes_page.check_payer_fio(payer_fio)
        # Перейти к оплате
        taxes_page.click_payment_btn()
        # Проверка на наличие текста "Тест оплаты"
        assert taxes_page.verify_payment_page_loaded(), 'На странице не появилась форма для оплаты'

        # # Кнопка оплаты
        # taxes_page.click_success_payment_btn()
        # time.sleep(1)
        #
        # # Проверка на наличие текста "ОПЛАТА УСПЕШНО ПРОИЗВЕДЕНА!"
        # assert taxes_page.verify_payment_success(), 'Произошла ошибка при оплате'
    @pytest.mark.parametrize("doc_type, doc_num", [
        ('УИН', '18810578230828569031')
    ])
    @allure.feature('Проверка оплаты налогов')
    @allure.story('Проверка по УИН без штрафов')
    def test_payment_taxes_page_uin_no_arrears(self, appium_driver, doc_type, doc_num):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных оплаты налогов
        taxes_page = TaxesPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в оплату налогов
        payments_page.go_to_payment_taxes()
        # Проверка на наличие сохранённых документов
        saved_doc = taxes_page.check_saved_doc(doc_type=doc_type, doc_num=doc_num)
        if saved_doc:
            taxes_page.click_saved_doc(value=saved_doc)
        else:
            if taxes_page.check_add_doc_btn():
                # Добавляем документ
                taxes_page.click_add_document_button()
            # Выбор типа документа проверки
            taxes_page.choose_doc_type(doc_type)
            # Ввод данных для проверки
            taxes_page.set_document_data(doc_num=doc_num)
            # Кнопка проверки
            taxes_page.click_check_btn()

        assert taxes_page.verify_no_arrears(), 'Ошибка при поиске задолженностей'

    # @allure.feature('Проверка оплаты налогов')
    # @allure.story('Проверка по УИН со штрафами')
    # TODO нет реквизита УИН с задолженностью
    # def test_payment_taxes_page_uin_have_arrears(self, appium_driver):
    #     # Инициализация стартовой страницы
    #     start_page = StartPage(appium_driver)
    #     # Инициализация страницы с выбором типа платежа
    #     payments_page = PaymentsPage(appium_driver)
    #     # Инициализация страницы с вводом данных оплаты налогов
    #     taxes_page = TaxesPage(appium_driver)
    #
    #     # Переход в страницу с платежами
    #     start_page.go_to_payments()
    #     # Переход в оплату налогов
    #     payments_page.go_to_payment_taxes()
    #     # Выбор типа документа проверки
    #     taxes_page.choose_doc_type('УИН')
    #     # Ввод данных для проверки
    #     taxes_page.set_document_data(doc_num='540363052918')
    #     # Кнопка проверки
    #     taxes_page.click_check_btn()
    #     # Заполнение фио плательщика
    #     taxes_page.check_payer_fio('Антонио Бандерас')
    #     # Перейти к оплате
    #     taxes_page.click_payment_btn()
    #     # Подтверждение оплаты
    #     taxes_page.click_success_payment_btn()
    #
    #     assert taxes_page.verify_payment_success(), 'Не удалось произвести оплату'
