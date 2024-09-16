import time
import pytest
from pages.payments.mvd_page import MVDPage
from pages.start_page import StartPage
from pages.payments.payments_page import PaymentsPage
import allure
from utils.screenshot_helper import take_screenshot


@pytest.mark.usefixtures("uninstall_app")
class TestSearchFinesMVD:
    @allure.feature('Проверка штрафов МВД')
    @pytest.mark.group1
    @allure.story('Проверка по паспорту иностранного гражданина без штрафов')
    @pytest.mark.parametrize("doc_number, doc_category, full_doc_category", [
        ('FA6169954', 'Паспорт', 'Паспорт иностранного гражданина')
    ])
    def test_no_fines_mvd(self, appium_driver, doc_number, doc_category, full_doc_category, uninstall_app):
        # Инициализация страниц
        start_page = StartPage(appium_driver)
        payments_page = PaymentsPage(appium_driver)
        mvd_page = MVDPage(appium_driver)
        take_screenshot(driver=appium_driver, test_name='test_no_fines_mvd',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_launch_app")

        # Переход на страницу с платежами
        start_page.go_to_payments()
        take_screenshot(driver=appium_driver, test_name='test_no_fines_mvd',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_to_payments_page")
        # Переход в поиск штрафов МВД
        payments_page.go_to_fines_mvd()
        take_screenshot(driver=appium_driver, test_name='test_no_fines_mvd',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_to_mvd_page")

        # Проверка на наличие сохранённых документов
        saved_doc = mvd_page.check_saved_doc(doc_number=doc_number, doc_category=doc_category)
        if saved_doc:
            mvd_page.click_saved_doc(value=saved_doc)
            take_screenshot(driver=appium_driver, test_name='test_no_fines_mvd',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_click_saved_doc")
        else:
            if mvd_page.check_add_doc_btn():
                # Добавляем документ
                mvd_page.add_doc()
                take_screenshot(driver=appium_driver, test_name='test_no_fines_mvd',
                                folder_name='payment_page',
                                screenshot_name=f"screen_after_click_add_doc_btn")
            # Ввод данных для проверки
            mvd_page.set_data(doc_number=doc_number, doc_category=full_doc_category)
            take_screenshot(driver=appium_driver, test_name='test_no_fines_mvd',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_set_data_{doc_category}_{doc_number}")
            # Запуск проверки
            mvd_page.click_check_btn()
            take_screenshot(driver=appium_driver, test_name='test_no_fines_mvd',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_click_check_btn")

        assert mvd_page.verify_no_fines(), \
            f'Штрафы были найдены или произошла ошибка при проверке штрафов - {doc_category} {doc_number}'
        take_screenshot(driver=appium_driver, test_name='test_no_fines_mvd',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_verify_no_fines")
        uninstall_app()

    @pytest.mark.parametrize("doc_number, doc_category, full_doc_category, payer_fio", [
        ('FA2684557', 'Паспорт', 'Паспорт иностранного гражданина', 'Антонио Луковый')
    ])
    @allure.feature('Проверка штрафов МВД')
    @pytest.mark.group2
    @allure.story('Проверка по паспорту иностранного гражданина со штрафами')
    def test_have_fines_mvd(self, appium_driver, doc_number, doc_category, full_doc_category, payer_fio):
        start_page = StartPage(appium_driver)
        payments_page = PaymentsPage(appium_driver)
        mvd_page = MVDPage(appium_driver)
        take_screenshot(driver=appium_driver, test_name='test_have_fines_mvd',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_launch_app")

        # Переход на страницу с платежами
        start_page.go_to_payments()
        take_screenshot(driver=appium_driver, test_name='test_have_fines_mvd',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_to_payments_page")
        # Переход в поиск штрафов МВД
        payments_page.go_to_fines_mvd()
        take_screenshot(driver=appium_driver, test_name='test_have_fines_mvd',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_go_to_mvd_page")
        # Проверка на наличие сохранённых документов
        saved_doc = mvd_page.check_saved_doc(doc_number=doc_number, doc_category=doc_category)
        if saved_doc:
            mvd_page.click_saved_doc(value=saved_doc)
            take_screenshot(driver=appium_driver, test_name='test_have_fines_mvd',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_click_saved_doc")
        else:
            if mvd_page.check_add_doc_btn():
                # Добавляем документ
                mvd_page.add_doc()
                take_screenshot(driver=appium_driver, test_name='test_have_fines_mvd',
                                folder_name='payment_page',
                                screenshot_name=f"screen_after_click_add_doc")
            # Ввод данных для проверки
            mvd_page.set_data(doc_number=doc_number, doc_category=full_doc_category)
            take_screenshot(driver=appium_driver, test_name='test_have_fines_mvd',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_set_data_{doc_category}_{doc_number}")
            # Запуск проверки
            mvd_page.click_check_btn()
            take_screenshot(driver=appium_driver, test_name='test_have_fines_mvd',
                            folder_name='payment_page',
                            screenshot_name=f"screen_after_click_check_btn")

        time.sleep(2)
        # Переход в страницу с оплатой
        mvd_page.check_payer_fio(fio=payer_fio)
        take_screenshot(driver=appium_driver, test_name='test_have_fines_mvd',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_check_payer_fio")
        mvd_page.click_payment_btn()
        take_screenshot(driver=appium_driver, test_name='test_have_fines_mvd',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_click_payment_btn")
        assert mvd_page.verify_payment_page_loaded(), \
            f'На странице не появилась форма для оплаты - {doc_category} {doc_number}'
        take_screenshot(driver=appium_driver, test_name='test_have_fines_mvd',
                        folder_name='payment_page',
                        screenshot_name=f"screen_after_verify_payment_page_loaded")
        # # Проверка на наличие текста "Тест оплаты"
        # assert mvd_page.check_test_payment_text(), 'На странице не появился текст для тестовой оплаты'
        #
        #
        # # Кнопка оплаты
        # mvd_page.click_success_payment_btn()
        # time.sleep(1)
        #
        # # Проверка на наличие текста "ОПЛАТА УСПЕШНО ПРОИЗВЕДЕНА!"
        # assert mvd_page.verify_payment_success(), 'Произошла ошибка при оплате'
