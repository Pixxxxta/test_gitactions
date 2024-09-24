import time
import pytest
from pages.services.payments.fines_gibdd_page import GIBDDPage
from pages.start_page import StartPage
from pages.services.payments.payments_page import PaymentsPage
import allure


class TestSearchFinesGIBDD:
    @allure.feature('Проверка штрафов ГИБДД')
    @allure.story('Проверка по госномеру автомобиля без штрафов')
    @pytest.mark.parametrize("doc_number, region, doc_category, doc_type", [
        ('В864РУ', '102', 'Госномер', 'Автомобиль')
    ])
    def test_no_fines_car_number(self, appium_driver, doc_number, region, doc_category, doc_type):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных поиска штрафов МВД
        gibdd_page = GIBDDPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в поиск штрафов ГИБДД
        payments_page.go_to_fines_gibdd()
        # Поиск среди прошлых проверок
        saved_doc = gibdd_page.check_saved_doc(doc_number=doc_number, doc_category=doc_category, region=region)
        if saved_doc:
            gibdd_page.click_saved_doc(value=saved_doc)
        else:
            if gibdd_page.check_add_doc_btn():
                # Добавляем документ
                gibdd_page.add_doc()
            # Выбор типа документа
            gibdd_page.choose_doc_type(doc_type)
            # Вставляем номер
            gibdd_page.set_car_number(doc_number=doc_number, region=region)
            # Запуск проверки
            gibdd_page.click_check_btn()

        assert gibdd_page.verify_no_fines(), 'Произошла ошибка при нахождении штрафов'

    @pytest.mark.parametrize("doc_number, region, doc_category, doc_type, payer_fio", [
        ('А555АА', '16', 'Госномер', 'Автомобиль', 'Брюс Уилис')
    ])
    @allure.feature('Проверка штрафов ГИБДД')
    @allure.story('Проверка по госномеру автомобиля со штрафами')
    def test_have_fines_car_number(self, appium_driver, doc_number, region, doc_category, doc_type, payer_fio):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных поиска штрафов МВД
        gibdd_page = GIBDDPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в поиск штрафов ГИБДД
        payments_page.go_to_fines_gibdd()
        # Поиск среди прошлых проверок
        saved_doc = gibdd_page.check_saved_doc(doc_number=doc_number, doc_category=doc_category, region=region)
        if saved_doc:
            gibdd_page.click_saved_doc(value=saved_doc)
        else:
            if gibdd_page.check_add_doc_btn():
                # Добавляем документ
                gibdd_page.add_doc()
            # Выбор типа документа
            gibdd_page.choose_doc_type(doc_type)
            # Вставляем номер
            gibdd_page.set_car_number(doc_number=doc_number, region=region)
            # Запуск проверки
            gibdd_page.click_check_btn()
        # Проверка на наличие ФИО
        time.sleep(1)
        gibdd_page.check_payer_fio(payer_fio)
        # Кнопка оплаты штрафов
        gibdd_page.click_payment_btn()

        assert gibdd_page.verify_payment_page_loaded(), 'Страница с оплатой не загружена'

    @pytest.mark.parametrize("doc_number, doc_category, doc_type", [
        ('9905723885', 'Водительское удостоверение', 'Водитель')
    ])
    @allure.feature('Проверка штрафов ГИБДД')
    @allure.story('Проверка по водительскому удостоверению без штрафов')
    def test_no_fines_driver_num(self, appium_driver, doc_number, doc_category, doc_type):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных поиска штрафов МВД
        gibdd_page = GIBDDPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в поиск штрафов ГИБДД
        payments_page.go_to_fines_gibdd()
        # Поиск среди прошлых проверок
        saved_doc = gibdd_page.check_saved_doc(doc_number=doc_number, doc_category=doc_category)
        if saved_doc:
            gibdd_page.click_saved_doc(value=saved_doc)
        else:
            if gibdd_page.check_add_doc_btn():
                # Добавляем документ
                gibdd_page.add_doc()
            # Выбор типа документа
            gibdd_page.choose_doc_type(doc_type)
            # Вставляем номер
            gibdd_page.set_driver_number(doc_number=doc_number)
            # Запуск проверки
            gibdd_page.click_check_btn()

        assert gibdd_page.verify_no_fines(), 'Произошла ошибка при нахождении штрафов'

    @pytest.mark.parametrize("doc_number, doc_category, doc_type", [
        ('1231231231', 'Водительское удостоверение', 'Водитель')
    ])
    @allure.feature('Проверка штрафов ГИБДД')
    @allure.story('Проверка по водительскому удостоверению со штрафами')
    def test_have_fines_driver_num(self, appium_driver, doc_number, doc_category, doc_type):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных поиска штрафов МВД
        gibdd_page = GIBDDPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в поиск штрафов ГИБДД
        payments_page.go_to_fines_gibdd()
        # Поиск среди прошлых проверок
        saved_doc = gibdd_page.check_saved_doc(doc_number=doc_number, doc_category=doc_category)
        if saved_doc:
            gibdd_page.click_saved_doc(value=saved_doc)
        else:
            if gibdd_page.check_add_doc_btn():
                # Добавляем документ
                gibdd_page.add_doc()
            # Выбор типа документа
            gibdd_page.choose_doc_type(doc_type)
            # Вставляем номер
            gibdd_page.set_driver_number(doc_number=doc_number)
            # Запуск проверки
            gibdd_page.click_check_btn()
        # Кнопка оплаты штрафов
        gibdd_page.click_payment_btn()

        assert gibdd_page.verify_payment_page_loaded(), 'Страница с оплатой не загружена'

    @pytest.mark.parametrize("doc_number, doc_category, doc_type", [
        ('18810578230828569031', 'УИН', 'УИН')
    ])
    @allure.feature('Проверка штрафов ГИБДД')
    @allure.story('Проверка по УИН без штрафов')
    def test_no_fines_UIN(self, appium_driver, doc_number, doc_category, doc_type):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных поиска штрафов МВД
        gibdd_page = GIBDDPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в поиск штрафов ГИБДД
        payments_page.go_to_fines_gibdd()
        # Проверка на наличие сохранённых документов
        if gibdd_page.check_add_doc_btn():
            # Добавляем документ
            gibdd_page.add_doc()
        # Выбор типа документа
        gibdd_page.choose_doc_type(doc_type)
        # Вставляем номер
        gibdd_page.set_UIN_number(uin=doc_number)
        # Запуск проверки
        gibdd_page.click_check_btn()

        assert gibdd_page.verify_no_fines(), 'Произошла ошибка при нахождении штрафов'

    @pytest.mark.parametrize("doc_number, doc_category, doc_type", [
        ('18810044200001105533', 'УИН', 'УИН')
    ])
    @allure.feature('Проверка штрафов ГИБДД')
    @allure.story('Проверка по УИН со штрафами')
    def test_have_fines_UIN(self, appium_driver, doc_number, doc_category, doc_type):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных поиска штрафов МВД
        gibdd_page = GIBDDPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в поиск штрафов ГИБДД
        payments_page.go_to_fines_gibdd()
        # Проверка на наличие сохранённых документов
        if gibdd_page.check_add_doc_btn():
            # Добавляем документ
            gibdd_page.add_doc()
        # Выбор типа документа
        gibdd_page.choose_doc_type(doc_type)
        time.sleep(1)
        # Вставляем номер
        gibdd_page.set_UIN_number(uin=doc_number)
        # Запуск проверки
        gibdd_page.click_check_btn()
        # Кнопка оплаты штрафов
        gibdd_page.click_payment_btn()

        assert gibdd_page.verify_payment_page_loaded(), 'Страница с оплатой не загружена'
