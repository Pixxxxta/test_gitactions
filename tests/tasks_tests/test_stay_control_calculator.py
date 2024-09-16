import pytest

from pages.start_page import StartPage
from pages.tasks.tasks_page import TasksPage
from pages.tasks.stay_control_calculator_page import StayControlCalculatorPage
from utils.screenshot_helper import take_screenshot
import allure


class TestStayControlCalculator:
    @pytest.mark.parametrize("first_entry_date", "end_date", [('01012024', 'end_date')])
    @allure.feature('Проверка калькулятора контроля сроков пребывания')
    @pytest.mark.group1
    def test_calc_control(self, appium_driver, first_entry_date, end_date):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)
        # Инициализация страницы с калькулятором срока пребывания
        calc_page = StayControlCalculatorPage(appium_driver)
        take_screenshot(driver=appium_driver, test_name='test_calc_control',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_launch_app")
        start_page.go_to_tasks()
        take_screenshot(driver=appium_driver, test_name='test_calc_control',
                        folder_name='main_page',
                        screenshot_name=f"screen_after_go_to_tasks_page")

        tasks_page.go_to_calc()
        take_screenshot(driver=appium_driver, test_name='test_calc_control',
                        folder_name='tasks_page',
                        screenshot_name=f"screen_after_go_to_calc")

        calc_page.close_info_page()
        take_screenshot(driver=appium_driver, test_name='test_calc_control',
                        folder_name='calc_page',
                        screenshot_name=f"screen_after_close_info_page")
        calc_page.set_first_entry_date(date=first_entry_date)
        take_screenshot(driver=appium_driver, test_name='test_calc_control',
                        folder_name='calc_page',
                        screenshot_name=f"screen_after_set_first_entry_date")
        calc_page.click_ready_btn()
        take_screenshot(driver=appium_driver, test_name='test_calc_control',
                        folder_name='calc_page',
                        screenshot_name=f"screen_after_click_ready_btn")

        assert calc_page.verify_end_date_of_stay(end_date=end_date), \
            'Отобразилась неправильная дата окончания пребывания'
        take_screenshot(driver=appium_driver, test_name='test_calc_control',
                        folder_name='calc_page',
                        screenshot_name=f"screen_after_verify_end_date_of_stay")

        # assert calc_page.verify_end_date_of_stay(
        #     end_date='c 01.01.2024 по 28.06.2024'), \
        #     'Отобразилась неправильная дата окончания пребывания'


