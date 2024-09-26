import time

from pages.start_page import StartPage
from pages.services.tasks.tasks_page import TasksPage
from pages.services.tasks.check_patent_page import CheckPatentPage


class TestCheckPatent:
    def test_check_patent(self, appium_driver):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)
        # Инициализация страницы с резюме
        check_patent_page = CheckPatentPage(appium_driver)

        start_page.go_to_tasks()
        tasks_page.go_to_check_patent()
        check_patent_page.close_rm_window()
        time.sleep(1)
        check_patent_page.set_patent_data('77 2204315436')
        time.sleep(1)
        check_patent_page.set_blank_data('РМ1111111')
        time.sleep(1)
        check_patent_page.set_passport('FA6169953')
        time.sleep(1)
        check_patent_page.press_back_btn()
        time.sleep(1)
        check_patent_page.swipe_down()
        time.sleep(1)
        check_patent_page.click_check_btn()
        # Ввод капчи пока только руками
        assert False
