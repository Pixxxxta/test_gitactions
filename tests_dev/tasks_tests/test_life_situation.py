from pages.start_page import StartPage
from pages.tasks.tasks_page import TasksPage


class TestLifeSituations:
    def test_go_to_naimix(self, appium_driver):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)

        start_page.go_to_tasks()
        tasks_page.go_to_naimix()

        assert tasks_page.check_current_url('naimix.info'), 'Страница naimix не загружена'

    def test_go_to_halal_card(self, appium_driver):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)

        start_page.go_to_tasks()
        tasks_page.go_to_halal_card()

        assert tasks_page.check_current_url('halalcard.ru'), 'Не произошёл переход на страницу halalcard.ru'

    def test_go_to_b24(self, appium_driver):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)

        start_page.go_to_tasks()
        tasks_page.go_to_b24()

        assert tasks_page.check_current_url('https://b24-d7ybaa.bitrix24.site'), 'Не произошёл переход на страницу https://b24-d7ybaa.bitrix24.site'
