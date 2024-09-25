import allure
from pages.services.payments.payment_taxes_page import TaxesPage
from pages.start_page import StartPage
from pages.services.payments.payments_page import PaymentsPage
import pytest
from utils.screenshot_helper import take_screenshot
from pages.services.services_page import ServicesPage


class TestTaxes:
    @pytest.mark.parametrize("doc_type, doc_num", [
        ('ИНН', '780204893183')
    ])
    @pytest.mark.group1
    @allure.feature('Проверка оплаты налогов')
    @allure.story('Проверка по ИНН без штрафов')
    def test_payment_taxes_page_inn_no_arrears(self, appium_driver, doc_type, doc_num):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с выбором типа платежа
        services_page = ServicesPage(appium_driver)
        # Инициализация страницы с вводом данных оплаты налогов
        taxes_page = TaxesPage(appium_driver)

        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_no_arrears',
                        folder_name='start_page',
                        screenshot_name="screen_after_choose_language")
        # Переход в страницу с сервисами
        start_page.go_to_services()
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_no_arrears',
                        folder_name='start_page',
                        screenshot_name=f"screen_after_go_to_services")
        # Переход в оплату налогов
        services_page.go_to_payment_taxes()
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_no_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_go_to_payment_taxes")
        # # Проверка на наличие сохранённых документов
        # saved_doc = taxes_page.check_saved_doc(doc_type=doc_type, doc_num=doc_num)
        # if saved_doc:
        #     taxes_page.click_saved_doc(value=saved_doc)
        #     take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_no_arrears',
        #                     folder_name='payments_page',
        #                     screenshot_name=f"screen_after_click_saved_doc")
        # else:
        #     if taxes_page.check_add_doc_btn():
        #         # Добавляем документ
        #         taxes_page.click_add_document_button()
        #         take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_no_arrears',
        #                         folder_name='payments_page',
        #                         screenshot_name=f"screen_after_click_add_doc")
        # Выбор типа документа проверки
        taxes_page.close_info_page()
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_no_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_close_info_page")
        taxes_page.choose_doc_type(doc_type)
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_no_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_choose_doc_{doc_type}")
        # Ввод данных для проверки
        taxes_page.set_document_data(doc_num=doc_num)
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_no_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_input_doc_num_{doc_num}")
        # Кнопка проверки
        taxes_page.click_check_btn()

        assert taxes_page.verify_no_arrears(), f'Ошибка при поиске задолженностей - {doc_type} - {doc_num}'
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_no_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_click_check_btn")
        start_page.reset_user()

    @pytest.mark.parametrize("doc_type, doc_num, payer_fio", [
        ('ИНН', '540363052918', 'Антонио Бандерас')
    ])
    @pytest.mark.group2
    @allure.feature('Проверка оплаты налогов')
    @allure.story('Проверка по ИНН со штрафами')
    def test_payment_taxes_page_inn_have_arrears(self, appium_driver, doc_type, doc_num, payer_fio):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с сервисами
        services_page = ServicesPage(appium_driver)
        # Инициализация страницы с вводом данных оплаты налогов
        taxes_page = TaxesPage(appium_driver)

        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_have_arrears',
                        folder_name='start_page',
                        screenshot_name="screen_after_choose_language")
        # Переход в страницу с сервисами
        start_page.go_to_services()
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_have_arrears',
                        folder_name='start_page',
                        screenshot_name=f"screen_after_go_to_payment")
        # Переход в оплату налогов
        services_page.go_to_payment_taxes()
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_have_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_go_to_payment_taxes")
        # Проверка на наличие сохранённых документов
        # saved_doc = taxes_page.check_saved_doc(doc_type=doc_type, doc_num=doc_num)
        # if saved_doc:
        #     taxes_page.click_saved_doc(value=saved_doc)
        #     take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_have_arrears',
        #                     folder_name='payments_page',
        #                     screenshot_name=f"screen_after_click_saved_doc")
        # else:
        #     if taxes_page.check_add_doc_btn():
        #         # Добавляем документ
        #         taxes_page.click_add_document_button()
        #         take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_have_arrears',
        #                         folder_name='payments_page',
        #                         screenshot_name=f"screen_after_click_add_doc")
        taxes_page.close_info_page()
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_have_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_close_info_page")
        # Выбор типа документа проверки
        taxes_page.choose_doc_type(doc_type)
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_have_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_choose_doc_{doc_type}")
        # Ввод данных для проверки
        taxes_page.set_document_data(doc_num=doc_num)
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_have_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_input_doc_num_{doc_num}")
        # Кнопка проверки
        taxes_page.click_check_btn()
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_have_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_click_check_btn")
        # Заполнение фио плательщика
        taxes_page.check_payer_fio(payer_fio)
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_have_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_payer_fio_input")
        # Перейти к оплате
        taxes_page.click_payment_btn()
        # Проверка на наличие загрузку страницы оплаты
        assert taxes_page.verify_payment_page_loaded(), f'На странице не появилась форма для оплаты - {doc_type} - {doc_num}'
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_inn_have_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_click_payment_btn")
        # # Кнопка оплаты
        # taxes_page.click_success_payment_btn()
        # time.sleep(1)
        #
        # # Проверка на наличие текста "ОПЛАТА УСПЕШНО ПРОИЗВЕДЕНА!"
        # assert taxes_page.verify_payment_success(), 'Произошла ошибка при оплате'
        start_page.reset_user()

    @pytest.mark.parametrize("doc_type, doc_num", [
        ('УИН', '18810578230828569031')
    ])
    @allure.feature('Проверка оплаты налогов')
    @pytest.mark.group3
    @allure.story('Проверка по УИН без штрафов')
    def test_payment_taxes_page_uin_no_arrears(self, appium_driver, doc_type, doc_num):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с сервисами
        services_page = ServicesPage(appium_driver)
        # Инициализация страницы с вводом данных оплаты налогов
        taxes_page = TaxesPage(appium_driver)

        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_uin_no_arrears',
                        folder_name='start_page',
                        screenshot_name="screen_after_choose_language")
        # Переход в страницу с платежами
        start_page.go_to_services()
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_uin_no_arrears',
                        folder_name='start_page',
                        screenshot_name=f"screen_after_go_to_payment")
        # Переход в оплату налогов
        services_page.go_to_payment_taxes()
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_uin_no_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_go_to_payment_taxes")
        # # Проверка на наличие сохранённых документов
        # saved_doc = taxes_page.check_saved_doc(doc_type=doc_type, doc_num=doc_num)
        # if saved_doc:
        #     taxes_page.click_saved_doc(value=saved_doc)
        #     take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_uin_no_arrears',
        #                     folder_name='payments_page',
        #                     screenshot_name=f"screen_after_click_saved_doc")
        # else:
        #     if taxes_page.check_add_doc_btn():
        #         # Добавляем документ
        #         taxes_page.click_add_document_button()

        taxes_page.close_info_page()
        # Выбор типа документа проверки
        taxes_page.choose_doc_type(doc_type)
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_uin_no_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_choose_doc_{doc_type}")
        # Ввод данных для проверки
        taxes_page.set_document_data(doc_num=doc_num)
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_uin_no_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_input_doc_num_{doc_num}")
        # Кнопка проверки
        taxes_page.click_check_btn()

        assert taxes_page.verify_no_arrears(), f'Ошибка при поиске задолженностей - {doc_type} - {doc_num}'
        take_screenshot(driver=appium_driver, test_name='test_payment_taxes_page_uin_no_arrears',
                        folder_name='payments_page',
                        screenshot_name=f"screen_after_click_check_btn")

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
