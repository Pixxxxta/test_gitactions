from pages.services.payments.state_duty_page import StateDutyPage
from pages.start_page import StartPage
from pages.services.payments.payments_page import PaymentsPage
import pytest
import allure


class TestPaymentStateDuty:
    @pytest.mark.parametrize("doc_number, fio, city", [
        ('FA6169953', 'АБДУРОСУЛОВ ДОСТОН', 'Москва')
    ])
    @allure.feature('Проверка оплаты госпошлины')
    @allure.story('За выдачу паспорта гражданина РФ - город Москва')
    def test_search_state_duty_moscow_city(self, appium_driver, doc_number, fio, city):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных для оплаты госпошлины
        state_duty_page = StateDutyPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в оплату госпошлины
        payments_page.go_to_payment_state_duty()
        # Заполнение полей, по умолчанию стоят поля:
        # duty_category - За выдачу паспорта гражданина РФ
        state_duty_page.set_data(doc_number=doc_number, fio=fio, city=city)

        # Проверяется, произошёл ли переход на страницу с оплатой
        assert state_duty_page.verify_payment_page_loaded_a3(), 'Не удалось перейти на страницу оплаты'

    @pytest.mark.parametrize("doc_number, fio, city", [
        ('FA6169953', 'АБДУРОСУЛОВ ДОСТОН', 'Казань')
    ])
    @allure.feature('Проверка оплаты госпошлины')
    @allure.story('За выдачу паспорта гражданина РФ - город Казань')
    def test_search_state_duty_kazan_city(self, appium_driver, doc_number, fio, city):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных для оплаты госпошлины
        state_duty_page = StateDutyPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в оплату госпошлины
        payments_page.go_to_payment_state_duty()
        # Заполнение полей, по умолчанию стоят поля:
        # duty_category - За выдачу паспорта гражданина РФ
        state_duty_page.set_data(doc_number=doc_number, fio=fio, city=city)

        # Проверяется, произошёл ли переход на страницу с оплатой
        assert state_duty_page.verify_payment_page_loaded_a3(), 'Не удалось перейти на страницу оплаты'

    @pytest.mark.parametrize("doc_number, fio, city", [
        ('FA6169953', 'АБДУРОСУЛОВ ДОСТОН', 'Санкт-Петербург')
    ])
    @allure.feature('Проверка оплаты госпошлины')
    @allure.story('За выдачу паспорта гражданина РФ - город Санкт-Петербург')
    def test_search_state_duty_spb_city(self, appium_driver, doc_number, fio, city):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных для оплаты госпошлины
        state_duty_page = StateDutyPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в оплату госпошлины
        payments_page.go_to_payment_state_duty()
        # Заполнение полей, по умолчанию стоят поля: duty_category - За выдачу паспорта гражданина РФ,
        # city - Санкт-Петербург, document - Паспорт иностранного гражданина,
        state_duty_page.set_data(doc_number=doc_number, fio=fio, city=city)

        # Проверяется, произошёл ли переход на страницу с оплатой
        assert state_duty_page.verify_payment_page_loaded_a3(), 'Не удалось перейти на страницу оплаты'

    @pytest.mark.parametrize("doc_number, fio, city", [
        ('FA6169953', 'АБДУРОСУЛОВ ДОСТОН', 'Нижний Новгород')
    ])
    @allure.feature('Проверка оплаты госпошлины')
    @allure.story('За выдачу паспорта гражданина РФ - город Нижний Новгород')
    def test_search_state_duty_nn_city(self, appium_driver, doc_number, fio, city):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных для оплаты госпошлины
        state_duty_page = StateDutyPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в оплату госпошлины
        payments_page.go_to_payment_state_duty()
        # Заполнение полей, по умолчанию стоят поля: duty_category - За выдачу паспорта гражданина РФ
        state_duty_page.set_data(doc_number=doc_number, fio=fio, city=city)

        # Проверяется, произошёл ли переход на страницу с оплатой
        assert state_duty_page.verify_payment_page_loaded_a3(), 'Не удалось перейти на страницу оплаты'

    @pytest.mark.parametrize("doc_number, fio, city", [
        ('FA6169953', 'АБДУРОСУЛОВ ДОСТОН', 'Самара')
    ])
    @allure.feature('Проверка оплаты госпошлины')
    @allure.story('За выдачу паспорта гражданина РФ - город Самара')
    def test_search_state_duty_samara_city(self, appium_driver, doc_number, fio, city):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        payments_page = PaymentsPage(appium_driver)
        # Инициализация страницы с вводом данных для оплаты госпошлины
        state_duty_page = StateDutyPage(appium_driver)

        # Переход в страницу с платежами
        start_page.go_to_payments()
        # Переход в оплату госпошлины
        payments_page.go_to_payment_state_duty()
        # Заполнение полей, по умолчанию стоят поля: duty_category - За выдачу паспорта гражданина РФ,
        # city - Самара, document - Паспорт иностранного гражданина,
        state_duty_page.set_data(doc_number=doc_number, fio=fio, city=city)

        # Проверяется, произошёл ли переход на страницу с оплатой
        assert state_duty_page.verify_payment_page_loaded_a3(), 'Не удалось перейти на страницу оплаты'

    # @allure.feature('Проверка оплаты госпошлины')
    # @allure.story('За выдачу паспорта гражданина РФ - город Другой')
    # def test_search_state_duty_another_city(self, appium_driver):
    #     # Инициализация стартовой страницы
    #     start_page = StartPage(appium_driver)
    #     # Инициализация страницы с выбором типа платежа
    #     payments_page = PaymentsPage(appium_driver)
    #     # Инициализация страницы с вводом данных для оплаты госпошлины
    #     state_duty_page = StateDutyPage(appium_driver)
    #
    #     # Переход в страницу с платежами
    #     start_page.go_to_payments()
    #     # Переход в оплату госпошлины
    #     payments_page.go_to_payment_state_duty()
    #     # Заполнение полей, по умолчанию стоят поля:
    #     # duty_category - За выдачу паспорта гражданина РФ, city - Москва, document - Паспорт иностранного гражданина,
    #     state_duty_page.set_data(city='Другой', doc_number='FA6169953', fio='АБДУРОСУЛОВ ДОСТОН')
    #
    #     # Проверяется, произошёл ли переход на страницу с оплатой
    #     assert state_duty_page.verify_payment_page_loaded(), 'Не удалось перейти на страницу оплаты'
