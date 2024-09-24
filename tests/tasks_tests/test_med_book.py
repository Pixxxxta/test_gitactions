import time

from pages.start_page import StartPage
from pages.tasks.tasks_page import TasksPage
from pages.tasks.med_book_page import MedBookPage


class TestResume:
    def test_med_book_have_info(self, appium_driver):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)
        # Инициализация страницы с мед книжкой
        med_book_page = MedBookPage(appium_driver)

        start_page.go_to_tasks()
        tasks_page.go_to_med_book()
        time.sleep(2)

        med_book_page.close_rm_window()
        med_book_page.set_med_book_data('1111')
        time.sleep(1)
        med_book_page.click_check_btn()

        assert med_book_page.verify_med_book_data(), 'Странца с данными не загружена'

    def test_med_book_no_info(self, appium_driver):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)
        # Инициализация страницы с мед книжкой
        med_book_page = MedBookPage(appium_driver)

        start_page.go_to_tasks()
        tasks_page.go_to_med_book()
        time.sleep(2)

        med_book_page.close_rm_window()
        med_book_page.set_med_book_data('12345678')
        time.sleep(1)
        med_book_page.click_check_btn()

        assert med_book_page.verify_med_book_data_not_found(), 'Странца с данными не загружена'
