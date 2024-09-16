import time
import pytest
from pages.payments.fines_gibdd_page import GIBDDPage
from pages.start_page import StartPage
from pages.payments.payments_page import PaymentsPage
import allure
from utils.screenshot_helper import take_screenshot


class TestSearchFinesGIBDD:
    @allure.feature('Проверка штрафов ГИБДД')
    @allure.story('Проверка по госномеру автомобиля без штрафов')
    @pytest.mark.group1
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
        take_screenshot(driver=appium_driver, test_name='test_no_fines_car_number',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_launch_app")

        # Переход в страницу с платежами
        start_page.go_to_payments()
        take_screenshot(driver=appium_driver, test_name='test_no_fines_car_number',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_to_payment_page")
        # Переход в поиск штрафов ГИБДД
        payments_page.go_to_fines_gibdd()
        take_screenshot(driver=appium_driver, test_name='test_no_fines_car_number',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_payment_gibdd_page")
        # Поиск среди прошлых проверок
        saved_doc = gibdd_page.check_saved_doc(doc_number=doc_number, doc_category=doc_category, region=region)
        take_screenshot(driver=appium_driver, test_name='test_no_fines_car_number',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_check_saved_doc_page")
        if saved_doc:
            gibdd_page.click_saved_doc(value=saved_doc)
            take_screenshot(driver=appium_driver, test_name='test_no_fines_car_number',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_click_saved_doc")
        else:
            if gibdd_page.check_add_doc_btn():
                # Добавляем документ
                gibdd_page.add_doc()
                take_screenshot(driver=appium_driver, test_name='test_no_fines_car_number',
                                folder_name='payment_page',
                                screenshot_name=f"screen_after_click_add_doc_btn")
            # Выбор типа документа
            gibdd_page.choose_doc_type(doc_type)
            take_screenshot(driver=appium_driver, test_name='test_no_fines_car_number',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_choose_doc_type_{doc_type}")
            # Вставляем номер
            gibdd_page.set_car_number(doc_number=doc_number, region=region)
            take_screenshot(driver=appium_driver, test_name='test_no_fines_car_number',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_input_car_num_{doc_number}_{region}")
            # Запуск проверки
            gibdd_page.click_check_btn()
            take_screenshot(driver=appium_driver, test_name='test_no_fines_car_number',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_click_check_btn")

        assert gibdd_page.verify_no_fines(), f'Произошла ошибка при нахождении штрафов - {doc_type} {doc_number} {region}'
        take_screenshot(driver=appium_driver, test_name='test_no_fines_car_number',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_verify_no_fines")

    @pytest.mark.parametrize("doc_number, region, doc_category, doc_type, payer_fio", [
        ('А555АА', '16', 'Госномер', 'Автомобиль', 'Брюс Уилис')
    ])
    @allure.feature('Проверка штрафов ГИБДД')
    @pytest.mark.group2
    @allure.story('Проверка по госномеру автомобиля со штрафами')
    def test_have_fines_car_number(self, appium_driver, doc_number, region, doc_category, doc_type, payer_fio):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных поиска штрафов МВД
        gibdd_page = GIBDDPage(appium_driver)
        take_screenshot(driver=appium_driver, test_name='test_have_fines_car_number',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_launch_app")

        # Переход в страницу с платежами
        start_page.go_to_payments()
        take_screenshot(driver=appium_driver, test_name='test_have_fines_car_number',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_to_payment_page")
        # Переход в поиск штрафов ГИБДД
        payments_page.go_to_fines_gibdd()
        take_screenshot(driver=appium_driver, test_name='test_have_fines_car_number',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_to_gibdd_page")
        # Поиск среди прошлых проверок
        saved_doc = gibdd_page.check_saved_doc(doc_number=doc_number, doc_category=doc_category, region=region)
        if saved_doc:
            gibdd_page.click_saved_doc(value=saved_doc)
            take_screenshot(driver=appium_driver, test_name='test_have_fines_car_number',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_click_on_saved_doc")
        else:
            if gibdd_page.check_add_doc_btn():
                # Добавляем документ
                gibdd_page.add_doc()
                take_screenshot(driver=appium_driver, test_name='test_have_fines_car_number',
                                folder_name='payment_page',
                                screenshot_name=f"screen_after_click_add_btn")
            # Выбор типа документа
            gibdd_page.choose_doc_type(doc_type)
            take_screenshot(driver=appium_driver, test_name='test_have_fines_car_number',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_choose_doc_type")
            # Вставляем номер
            gibdd_page.set_car_number(doc_number=doc_number, region=region)
            take_screenshot(driver=appium_driver, test_name='test_have_fines_car_number',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_input_car_number_{doc_number}_{region}")
            # Запуск проверки
            gibdd_page.click_check_btn()
            take_screenshot(driver=appium_driver, test_name='test_have_fines_car_number',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_click_check_btn")
        # Проверка на наличие ФИО
        time.sleep(1)
        gibdd_page.check_payer_fio(payer_fio)
        take_screenshot(driver=appium_driver, test_name='test_have_fines_car_number',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_input_payer_fio")
        # Кнопка оплаты штрафов
        gibdd_page.click_payment_btn()
        take_screenshot(driver=appium_driver, test_name='test_have_fines_car_number',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_click_payment_btn")

        assert gibdd_page.verify_payment_page_loaded(), \
            f'На странице не появилась форма для оплаты - {doc_category} {doc_number} {region}'
        take_screenshot(driver=appium_driver, test_name='test_have_fines_car_number',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_verify_payment_page_loaded")

        # # Проверка на наличие текста "Тест оплаты"
        # assert gibdd_page.check_test_payment_text(), 'На странице не появился текст для тестовой оплаты'
        #
        # # Кнопка оплаты
        # gibdd_page.click_success_payment_btn()
        # time.sleep(1)
        #
        # # Проверка на наличие текста "ОПЛАТА УСПЕШНО ПРОИЗВЕДЕНА!"
        # assert gibdd_page.verify_payment_success(), 'Произошла ошибка при оплате'

    @pytest.mark.parametrize("doc_number, doc_category, doc_type", [
        ('9905723885', 'Водительское удостоверение', 'Водитель')
    ])
    @allure.feature('Проверка штрафов ГИБДД')
    @pytest.mark.group3
    @allure.story('Проверка по водительскому удостоверению без штрафов')
    def test_no_fines_driver_num(self, appium_driver, doc_number, doc_category, doc_type):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных поиска штрафов МВД
        gibdd_page = GIBDDPage(appium_driver)
        take_screenshot(driver=appium_driver, test_name='test_no_fines_driver_num',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_launch_app")

        # Переход в страницу с платежами
        start_page.go_to_payments()
        take_screenshot(driver=appium_driver, test_name='test_no_fines_driver_num',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_to_payment_page")
        # Переход в поиск штрафов ГИБДД
        payments_page.go_to_fines_gibdd()
        take_screenshot(driver=appium_driver, test_name='test_no_fines_driver_num',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_to_gibdd_page")
        # Поиск среди прошлых проверок
        saved_doc = gibdd_page.check_saved_doc(doc_number=doc_number, doc_category=doc_category)
        if saved_doc:
            gibdd_page.click_saved_doc(value=saved_doc)
            take_screenshot(driver=appium_driver, test_name='test_no_fines_driver_num',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_click_saved_doc")
        else:
            if gibdd_page.check_add_doc_btn():
                # Добавляем документ
                gibdd_page.add_doc()
                take_screenshot(driver=appium_driver, test_name='test_no_fines_driver_num',
                                folder_name='payment_page',
                                screenshot_name=f"screen_after_click_add_btn")
            # Выбор типа документа
            gibdd_page.choose_doc_type(doc_type)
            take_screenshot(driver=appium_driver, test_name='test_no_fines_driver_num',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_choose_doc_type")
            # Вставляем номер
            gibdd_page.set_driver_number(doc_number=doc_number)
            take_screenshot(driver=appium_driver, test_name='test_no_fines_driver_num',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_set_driver_number_{doc_number}")
            # Запуск проверки
            gibdd_page.click_check_btn()
            take_screenshot(driver=appium_driver, test_name='test_no_fines_driver_num',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_click_payment_btn")

        assert gibdd_page.verify_no_fines(), f'Произошла ошибка с поиском штрафов - {doc_category} {doc_number}'
        take_screenshot(driver=appium_driver, test_name='test_no_fines_driver_num',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_verify_no_fines")

    @pytest.mark.parametrize("doc_number, doc_category, doc_type", [
        ('1231231231', 'Водительское удостоверение', 'Водитель')
    ])
    @allure.feature('Проверка штрафов ГИБДД')
    @pytest.mark.group4
    @allure.story('Проверка по водительскому удостоверению со штрафами')
    def test_have_fines_driver_num(self, appium_driver, doc_number, doc_category, doc_type):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных поиска штрафов МВД
        gibdd_page = GIBDDPage(appium_driver)
        take_screenshot(driver=appium_driver, test_name='test_have_fines_driver_num',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_launch_app")

        # Переход в страницу с платежами
        start_page.go_to_payments()
        take_screenshot(driver=appium_driver, test_name='test_have_fines_driver_num',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_to_payments_page")
        # Переход в поиск штрафов ГИБДД
        payments_page.go_to_fines_gibdd()
        take_screenshot(driver=appium_driver, test_name='test_have_fines_driver_num',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_to_gibdd_page")
        # Поиск среди прошлых проверок
        saved_doc = gibdd_page.check_saved_doc(doc_number=doc_number, doc_category=doc_category)
        if saved_doc:
            gibdd_page.click_saved_doc(value=saved_doc)
            take_screenshot(driver=appium_driver, test_name='test_have_fines_driver_num',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_click_saved_doc")
        else:
            if gibdd_page.check_add_doc_btn():
                # Добавляем документ
                gibdd_page.add_doc()
                take_screenshot(driver=appium_driver, test_name='test_have_fines_driver_num',
                                folder_name='payment_page',
                                screenshot_name=f"screen_after_click_add_doc_btn")
            # Выбор типа документа
            gibdd_page.choose_doc_type(doc_type)
            take_screenshot(driver=appium_driver, test_name='test_have_fines_driver_num',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_choose_doc_type")
            # Вставляем номер
            gibdd_page.set_driver_number(doc_number=doc_number)
            take_screenshot(driver=appium_driver, test_name='test_have_fines_driver_num',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_set_driver_number_{doc_number}")
            # Запуск проверки
            gibdd_page.click_check_btn()
            take_screenshot(driver=appium_driver, test_name='test_have_fines_driver_num',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_click_check_btn")
        # Кнопка оплаты штрафов
        gibdd_page.click_payment_btn()
        take_screenshot(driver=appium_driver, test_name='test_have_fines_driver_num',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_click_payment_btn")

        assert gibdd_page.verify_payment_page_loaded(), \
            f'На странице не появилась форма для оплаты - {doc_category} {doc_number}'
        take_screenshot(driver=appium_driver, test_name='test_have_fines_driver_num',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_verify_payment_page_loaded")

        # # Проверка на наличие текста "Тест оплаты"
        # assert gibdd_page.check_test_payment_text(), 'На странице не появился текст для тестовой оплаты'
        #
        # # Кнопка оплаты
        # gibdd_page.click_success_payment_btn()
        # time.sleep(1)
        #
        # # Проверка на наличие текста "ОПЛАТА УСПЕШНО ПРОИЗВЕДЕНА!"
        # assert gibdd_page.verify_payment_success(), 'Произошла ошибка при оплате'

    @pytest.mark.parametrize("doc_number, doc_category, doc_type", [
        ('18810578230828569031', 'УИН', 'УИН')
    ])
    @allure.feature('Проверка штрафов ГИБДД')
    @pytest.mark.group5
    @allure.story('Проверка по УИН без штрафов')
    def test_no_fines_UIN(self, appium_driver, doc_number, doc_category, doc_type):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных поиска штрафов МВД
        gibdd_page = GIBDDPage(appium_driver)
        take_screenshot(driver=appium_driver, test_name='test_no_fines_UIN',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_launch_app")

        # Переход в страницу с платежами
        start_page.go_to_payments()
        take_screenshot(driver=appium_driver, test_name='test_no_fines_UIN',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_to_payments_page")
        # Переход в поиск штрафов ГИБДД
        payments_page.go_to_fines_gibdd()
        take_screenshot(driver=appium_driver, test_name='test_no_fines_UIN',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_to_gibdd_page")
        # Проверка на наличие сохранённых документов
        if gibdd_page.check_add_doc_btn():
            # Добавляем документ
            gibdd_page.add_doc()
            take_screenshot(driver=appium_driver, test_name='test_no_fines_UIN',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_click_add_doc_btn")
        # Выбор типа документа
        gibdd_page.choose_doc_type(doc_type)
        take_screenshot(driver=appium_driver, test_name='test_no_fines_UIN',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_choose_doc_type_{doc_type}")
        # Вставляем номер
        gibdd_page.set_UIN_number(uin=doc_number)
        take_screenshot(driver=appium_driver, test_name='test_no_fines_UIN',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_set_UIN_number_{doc_number}")
        # Запуск проверки
        gibdd_page.click_check_btn()
        take_screenshot(driver=appium_driver, test_name='test_no_fines_UIN',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_click_check_btn")

        assert gibdd_page.verify_no_fines(), f'Произошла ошибка при нахождении штрафов - {doc_category} {doc_number}'
        take_screenshot(driver=appium_driver, test_name='test_no_fines_UIN',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_verify_no_fines")

    @pytest.mark.parametrize("doc_number, doc_category, doc_type", [
        ('18810044200001105533', 'УИН', 'УИН')
    ])
    @allure.feature('Проверка штрафов ГИБДД')
    @pytest.mark.group6
    @allure.story('Проверка по УИН со штрафами')
    def test_have_fines_UIN(self, appium_driver, doc_number, doc_category, doc_type):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных поиска штрафов МВД
        gibdd_page = GIBDDPage(appium_driver)
        take_screenshot(driver=appium_driver, test_name='test_have_fines_UIN',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_launch_app")

        # Переход в страницу с платежами
        start_page.go_to_payments()
        take_screenshot(driver=appium_driver, test_name='test_have_fines_UIN',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_to_payments_page")
        # Переход в поиск штрафов ГИБДД
        payments_page.go_to_fines_gibdd()
        take_screenshot(driver=appium_driver, test_name='test_have_fines_UIN',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_to_gibdd_page")
        # Проверка на наличие сохранённых документов
        if gibdd_page.check_add_doc_btn():
            # Добавляем документ
            gibdd_page.add_doc()
            take_screenshot(driver=appium_driver, test_name='test_have_fines_UIN',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_click_add_doc_btn")
        # Выбор типа документа
        gibdd_page.choose_doc_type(doc_type)
        take_screenshot(driver=appium_driver, test_name='test_have_fines_UIN',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_choose_doc_type_{doc_type}")
        time.sleep(1)
        # Вставляем номер
        gibdd_page.set_UIN_number(uin=doc_number)
        take_screenshot(driver=appium_driver, test_name='test_have_fines_UIN',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_set_UIN_number_{doc_number}")
        # Запуск проверки
        gibdd_page.click_check_btn()
        take_screenshot(driver=appium_driver, test_name='test_have_fines_UIN',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_click_check_btn")
        # Кнопка оплаты штрафов
        gibdd_page.click_payment_btn()
        take_screenshot(driver=appium_driver, test_name='test_have_fines_UIN',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_click_payment_btn")

        assert gibdd_page.verify_payment_page_loaded(), \
            f'На странице не появилась форма для оплаты - {doc_category} {doc_number}'
        take_screenshot(driver=appium_driver, test_name='test_have_fines_UIN',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_verify_payment_page_loaded")
        # # Проверка на наличие текста "Тест оплаты"
        # assert gibdd_page.check_test_payment_text(), 'На странице не появился текст для тестовой оплаты'
        #
        # # Кнопка оплаты
        # gibdd_page.click_success_payment_btn()
        # time.sleep(1)
        #
        # # Проверка на наличие текста "ОПЛАТА УСПЕШНО ПРОИЗВЕДЕНА!"
        # assert gibdd_page.verify_payment_success(), 'Произошла ошибка при оплате'

