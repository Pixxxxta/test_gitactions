import time

import pytest

from pages.start_page import StartPage
from pages.tasks.tasks_page import TasksPage
from pages.tasks.med_book_page import MedBookPage
from utils.screenshot_helper import take_screenshot
import allure


class TestMedBook:
    @pytest.mark.parametrize("med_book_data", ['1111'])
    @allure.feature('Проверка медкнижки')
    @pytest.mark.group1
    @allure.story('Проверка с наличием информации')
    def test_med_book_have_info(self, appium_driver, med_book_data):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)
        # Инициализация страницы с мед книжкой
        med_book_page = MedBookPage(appium_driver)
        take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_launch_app")

        start_page.go_to_tasks()
        take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
                        folder_name='tasks_page',
                        screenshot_name=f"screen_after_go_to_tasks_page")
        # tasks_page.go_to_med_book()
        # take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
        #                 folder_name='tasks_page',
        #                 screenshot_name=f"screen_after_scroll_to_med_book")
        tasks_page.click_med_book_btn()
        take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
                        folder_name='tasks_page',
                        screenshot_name=f"screen_after_click_med_book_btn")
        med_book_page.close_rm_window()
        take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
                        folder_name='tasks_page',
                        screenshot_name=f"screen_after_close_subscribe_advert")
        med_book_page.set_med_book_data(med_book_data)
        take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
                        folder_name='tasks_page',
                        screenshot_name=f"screen_after_set_med_book_data - {med_book_data}")
        med_book_page.click_check_btn()
        take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
                        folder_name='tasks_page',
                        screenshot_name=f"screen_after_click_check_btn")

        assert med_book_page.verify_med_book_data(), f'Страница с данными не загружена - {med_book_data}'
        take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
                        folder_name='tasks_page',
                        screenshot_name=f"screen_after_verify_med_book_data")

    @pytest.mark.parametrize("med_book_data", ['12345678'])
    @allure.feature('Проверка медкнижки')
    @allure.story('Проверка без наличия информации')
    def test_med_book_no_info(self, appium_driver, med_book_data):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)
        # Инициализация страницы с мед книжкой
        med_book_page = MedBookPage(appium_driver)
        take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_launch_app")

        start_page.go_to_tasks()
        take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
                        folder_name='tasks_page',
                        screenshot_name=f"screen_after_go_to_tasks_page")
        tasks_page.go_to_med_book()
        take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
                        folder_name='tasks_page',
                        screenshot_name=f"screen_after_go_to_med_book_page")
        med_book_page.close_rm_window()
        take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
                        folder_name='tasks_page',
                        screenshot_name=f"screen_after_close_subscribe_advert")
        med_book_page.set_med_book_data(med_book_data)
        take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
                        folder_name='tasks_page',
                        screenshot_name=f"screen_after_go_med_book_page")
        take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
                        folder_name='tasks_page',
                        screenshot_name=f"screen_after_set_med_book_data - {med_book_data}")
        med_book_page.click_check_btn()
        take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
                        folder_name='tasks_page',
                        screenshot_name=f"screen_after_click_check_btn")

        assert med_book_page.verify_med_book_data_not_found(), f'Страница с данными не загружена - {med_book_data}'
        take_screenshot(driver=appium_driver, test_name='test_med_book_have_info',
                        folder_name='tasks_page',
                        screenshot_name=f"screen_after_verify_med_book_data")