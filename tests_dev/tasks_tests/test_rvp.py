import time

from pages.start_page import StartPage
from pages.tasks.tasks_page import TasksPage
from pages.tasks.rvp_vnj_page import RvpVnjPage


class TestRvpVnj:
    def test_rvp(self, appium_driver):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)
        # Инициализация страницы с проверкой РВП и ВНЖ
        rvp_vnj_page = RvpVnjPage(appium_driver)

        start_page.go_to_tasks()
        tasks_page.go_to_check_rvp_vnj()
        rvp_vnj_page.close_rm_window()
        time.sleep(1)
        rvp_vnj_page.choose_check_type('РВП')
        time.sleep(1)
        rvp_vnj_page.set_date(date='12112002')
        time.sleep(1)
        rvp_vnj_page.set_passport(passport_data='N11794079')
        time.sleep(1)
        rvp_vnj_page.choose_region(region='город федерального значения Санкт-Петербург', timeout=2)
        rvp_vnj_page.swipe_down()
        time.sleep(20)
        # Ввод капчи пока только руками
        rvp_vnj_page.click_check_btn()
        time.sleep(3)
        assert rvp_vnj_page.verify_rvp_found(), 'РВП не найдено'

    def test_vnj(self, appium_driver):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)
        # Инициализация страницы с проверкой РВП и ВНЖ
        rvp_vnj_page = RvpVnjPage(appium_driver)

        start_page.go_to_tasks()
        tasks_page.go_to_check_rvp_vnj()
        rvp_vnj_page.close_rm_window()
        time.sleep(1)
        rvp_vnj_page.choose_check_type('ВНЖ')
        time.sleep(1)
        rvp_vnj_page.set_date(date='12112002')
        time.sleep(1)
        rvp_vnj_page.set_passport(passport_data='N11794079')
        time.sleep(1)
        rvp_vnj_page.choose_region(region='город федерального значения Санкт-Петербург', timeout=2)
        rvp_vnj_page.swipe_down()
        time.sleep(20)
        # Ввод капчи пока только руками
        rvp_vnj_page.click_check_btn()
        time.sleep(3)
        assert rvp_vnj_page.verify_rvp_found(), 'РВП не найдено'
