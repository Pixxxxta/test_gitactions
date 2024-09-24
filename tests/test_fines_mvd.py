import time
import pytest
from pages.services.payments.mvd_page import MVDPage
from pages.start_page import StartPage
from pages.services.payments.payments_page import PaymentsPage
import allure


class TestSearchFinesMVD:
    @allure.feature('Проверка штрафов МВД')
    @allure.story('Проверка по паспорту иностранного гражданина без штрафов')
    @pytest.mark.parametrize("doc_number, doc_category, full_doc_category", [
        ('FA6169954', 'Паспорт', 'Паспорт иностранного гражданина')
    ])
    def test_no_fines(self, appium_driver, doc_number, doc_category, full_doc_category):
        # Инициализация страниц
        start_page = StartPage(appium_driver)
        payments_page = PaymentsPage(appium_driver)
        mvd_page = MVDPage(appium_driver)

        # Переход на страницу с платежами
        start_page.go_to_payments()
        # Переход в поиск штрафов МВД
        payments_page.go_to_fines_mvd()

        # Проверка на наличие сохранённых документов
        saved_doc = mvd_page.check_saved_doc(doc_number=doc_number, doc_category=doc_category)
        if saved_doc:
            mvd_page.click_saved_doc(value=saved_doc)
        else:
            if mvd_page.check_add_doc_btn():
                # Добавляем документ
                mvd_page.add_doc()
            # Ввод данных для проверки
            mvd_page.set_data(doc_number=doc_number, doc_category=full_doc_category)
            # Запуск проверки
            mvd_page.click_check_btn()

        assert mvd_page.verify_no_fines(), 'Штрафы были найдены или произошла ошибка при проверке штрафов'

    @pytest.mark.parametrize("doc_number, doc_category, full_doc_category", [
        ('FA2684557', 'Паспорт', 'Паспорт иностранного гражданина')
    ])
    @allure.feature('Проверка штрафов МВД')
    @allure.story('Проверка по паспорту иностранного гражданина со штрафами')
    def test_have_fines(self, appium_driver, doc_number, doc_category, full_doc_category):
        # Инициализация страниц
        start_page = StartPage(appium_driver)
        payments_page = PaymentsPage(appium_driver)
        mvd_page = MVDPage(appium_driver)

        # Переход на страницу с платежами
        start_page.go_to_payments()
        # Переход в поиск штрафов МВД
        payments_page.go_to_fines_mvd()

        # Проверка на наличие сохранённых документов
        saved_doc = mvd_page.check_saved_doc(doc_number=doc_number, doc_category=doc_category)
        if saved_doc:
            mvd_page.click_saved_doc(value=saved_doc)
        else:
            if mvd_page.check_add_doc_btn():
                # Добавляем документ
                mvd_page.add_doc()
            # Ввод данных для проверки
            mvd_page.set_data(doc_number=doc_number, doc_category=full_doc_category)
            # Запуск проверки
            mvd_page.click_check_btn()

        time.sleep(2)
        # Переход в страницу с оплатой
        mvd_page.go_to_payment()
        time.sleep(5)
        assert mvd_page.verify_payment_page_loaded, 'Страница с оплатой не загружена'
