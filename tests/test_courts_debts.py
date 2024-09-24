import allure
import pytest
from pages.services.payments.court_debts_page import CourtDebtsPage
from pages.start_page import StartPage
from pages.services.payments.payments_page import PaymentsPage


class TestCourtsDebts:
    @pytest.mark.parametrize("fio, birth_date, region", [
        ('Хазиев Дмитрий Артурович', '08.11.2002', 'Республика Башкортостан')
    ])
    @allure.feature('Проверка штрафов ФССП')
    @allure.story('Проверка без штрафов')
    def test_payment_courts_debts_page_no_arrears(self, appium_driver, fio, birth_date, region):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных судебных задолженностей
        court_debts_page = CourtDebtsPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в судебные задолженности
        payments_page.go_to_court_debts()
        # Ввод фио
        court_debts_page.set_fio(fio)
        # Ввод даты
        court_debts_page.set_date(birth_date)
        # Выбор региона
        court_debts_page.choose_region(region=region)
        # Кнопка проверки
        court_debts_page.click_check_btn()

        assert court_debts_page.verify_no_arrears(), 'Ошибка при поиске задолженностей'

    @pytest.mark.parametrize("fio, birth_date, region, payer_fio", [
        ('Максуди Иннокентий Рустэмович', '09.03.1986', 'Татарстан', 'Антонио Бандерас')
    ])
    @allure.feature('Проверка штрафов ФССП')
    @allure.story('Проверка со штрафами')
    def test_payment_courts_debts_page_have_arrears(self, appium_driver, fio, birth_date, region, payer_fio):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных оплаты налогов
        court_debts_page = CourtDebtsPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в судебные задолженности
        payments_page.go_to_court_debts()
        # Ввод фио
        court_debts_page.set_fio(fio)
        # Ввод даты
        court_debts_page.set_date(birth_date)
        # Выбор региона
        court_debts_page.choose_region(region=region)
        # Кнопка проверки
        court_debts_page.click_check_btn()
        # Заполнение фио плательщика
        court_debts_page.check_payer_fio(payer_fio)
        # Перейти к оплате
        court_debts_page.click_payment_btn()

        assert court_debts_page.verify_payment_page_loaded(), 'Не удалось перейти на странице с оплатой'
