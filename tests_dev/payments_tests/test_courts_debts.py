import time
import allure
import pytest
from pages.payments.court_debts_page import CourtDebtsPage
from pages.start_page import StartPage
from pages.payments.payments_page import PaymentsPage
from utils.screenshot_helper import take_screenshot


class TestCourtsDebts:

    @pytest.mark.parametrize("fio, birth_date, region", [
        ('Хазиев Дмитрий Артурович', '08.11.2002', 'Республика Башкортостан')
    ])
    @pytest.mark.group5
    @allure.feature('Проверка штрафов ФССП')
    @allure.story('Проверка без штрафов')
    def test_payment_courts_debts_page_no_arrears(self, appium_driver, fio, birth_date, region):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных судебных задолженностей
        court_debts_page = CourtDebtsPage(appium_driver)
        take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_no_arrears',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_launch_app")
        # Переход в страницу с платежами
        start_page.go_to_payments()
        take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_no_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_go_to_payment_page")
        # Переход в судебные задолженности
        payments_page.go_to_court_debts()
        take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_no_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_go_to_court_debts_page")
        # Проверка на наличие сохранённых документов
        saved_doc = court_debts_page.check_saved_doc(fio=fio)
        if saved_doc:
            court_debts_page.click_saved_doc(value=saved_doc)
        else:
            if court_debts_page.check_add_doc_btn():
                # Добавляем документ
                court_debts_page.add_doc()
            # Ввод фио
            court_debts_page.set_fio(fio)
            take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_no_arrears',
                            folder_name='payments_page',
                            screenshot_name=f"screen_after_input_fio_{fio}")
            # Ввод даты
            court_debts_page.set_date(birth_date)
            take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_no_arrears',
                            folder_name='payments_page',
                            screenshot_name=f"screen_after_input_date_{birth_date}")
            # Выбор региона
            court_debts_page.choose_region(region=region)
            take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_no_arrears',
                            folder_name='payments_page',
                            screenshot_name=f"screen_after_input_region_{region}")
            # Кнопка проверки
            court_debts_page.click_check_btn()
            take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_no_arrears',
                            folder_name='payments_page',
                            screenshot_name=f"screen_after_click_check_btn")

        assert court_debts_page.verify_no_arrears(), f'Ошибка при поиске задолженностей - {fio} {birth_date} {region}'
        take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_no_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_verify_no_arrears")

    @pytest.mark.parametrize("fio, birth_date, region, payer_fio", [
        ('Максуди Иннокентий Рустемович', '09.03.1986', 'Республика Татарстан (Татарстан)', 'Антонио Бандерас')
    ])
    @allure.feature('Проверка штрафов ФССП')
    @pytest.mark.group6
    @allure.story('Проверка со штрафами')
    def test_payment_courts_debts_page_have_arrears(self, appium_driver, fio, birth_date, region, payer_fio):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных оплаты налогов
        court_debts_page = CourtDebtsPage(appium_driver)
        take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_have_arrears',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_launch_app")
        # Переход в страницу с платежами
        start_page.go_to_payments()
        take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_have_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_go_to_payment_page")
        # Переход в судебные задолженности
        payments_page.go_to_court_debts()
        take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_have_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_go_to_court_debts_page")
        # Проверка на наличие сохранённых документов
        saved_doc = court_debts_page.check_saved_doc(fio=fio)
        if saved_doc:
            court_debts_page.click_saved_doc(value=saved_doc)
        else:
            if court_debts_page.check_add_doc_btn():
                # Добавляем документ
                court_debts_page.add_doc()
            # Ввод фио
            court_debts_page.set_fio(fio)
            take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_have_arrears',
                            folder_name='payments_page',
                            screenshot_name=f"screen_after_input_fio_{fio}")
            # Ввод даты
            court_debts_page.set_date(birth_date)
            take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_have_arrears',
                            folder_name='payments_page',
                            screenshot_name=f"screen_after_input_date_{birth_date}")
            # Выбор региона
            court_debts_page.choose_region(region=region)
            take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_have_arrears',
                            folder_name='payments_page',
                            screenshot_name=f"screen_after_input_region_{region}")
            # Кнопка проверки
            court_debts_page.click_check_btn()
            take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_have_arrears',
                            folder_name='payments_page',
                            screenshot_name=f"screen_after_click_check_btn")
        # Заполнение фио плательщика
        court_debts_page.check_payer_fio(payer_fio)
        take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_have_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_payer_fio_input")
        # Перейти к оплате
        court_debts_page.click_payment_btn()
        take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_have_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_click_payment_btn_before_verify_test")
        # Проверка на наличие появления формы оплаты
        assert court_debts_page.verify_payment_page_loaded(), f'На странице не появилась форма для оплаты - {fio} {birth_date} {region}'
        take_screenshot(driver=appium_driver, test_name='test_payment_courts_debts_page_have_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_click_payment_btn")
        # # Кнопка оплаты
        # court_debts_page.click_success_payment_btn()
        # time.sleep(1)
        #
        # # Проверка на наличие текста "ОПЛАТА УСПЕШНО ПРОИЗВЕДЕНА!"
        # assert court_debts_page.verify_payment_success(), 'Произошла ошибка при оплате'