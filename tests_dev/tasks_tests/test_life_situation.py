from pages.start_page import StartPage
from pages.services.tasks.tasks_page import TasksPage
from pages.services.services_page import ServicesPage
from utils.screenshot_helper import take_screenshot


class TestLifeSituations:
    def test_go_to_naimix(self, appium_driver):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с сервисами
        services_page = ServicesPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)
        take_screenshot(appium_driver, test_name='test_go_to_naimix', folder_name='main_page',
                        screenshot_name='screenshot_after_launch_app')

        start_page.go_to_services()
        take_screenshot(appium_driver, test_name='test_go_to_naimix', folder_name='services_page',
                        screenshot_name='screenshot_after_go_to_services')
        services_page.go_to_all_services()
        take_screenshot(appium_driver, test_name='test_go_to_naimix', folder_name='services_page',
                        screenshot_name='screenshot_after_go_to_all_services')
        services_page.go_to_task('Подработка рядом с домом')
        take_screenshot(appium_driver, test_name='test_go_to_naimix', folder_name='services_page',
                        screenshot_name='screenshot_after_go_to_task_Подработка рядом с домом')
        services_page.click_accept_google_chrome_btn()
        take_screenshot(appium_driver, test_name='test_go_to_naimix', folder_name='services_page',
                        screenshot_name='screenshot_after_click_accept_google_chrome_btn')
        assert tasks_page.check_current_url('naimix.info'), 'Страница naimix не загружена'
        take_screenshot(appium_driver, test_name='test_go_to_naimix', folder_name='services_page',
                        screenshot_name='screenshot_after_check_current_url')

    def test_go_to_halal_card(self, appium_driver):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с сервисами
        services_page = ServicesPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)

        start_page.go_to_services()
        take_screenshot(appium_driver, test_name='test_go_to_halal_card', folder_name='services_page',
                        screenshot_name='screenshot_after_go_to_services')
        services_page.go_to_all_services()
        take_screenshot(appium_driver, test_name='test_go_to_halal_card', folder_name='services_page',
                        screenshot_name='screenshot_after_go_to_all_services')
        services_page.go_to_task('HalalCard')
        take_screenshot(appium_driver, test_name='test_go_to_halal_card', folder_name='services_page',
                        screenshot_name='screenshot_after_go_to_task_HalalCard')
        services_page.click_accept_google_chrome_btn()
        take_screenshot(appium_driver, test_name='test_go_to_halal_card', folder_name='services_page',
                        screenshot_name='screenshot_after_click_accept_google_chrome_btn')
        assert tasks_page.check_current_url('halalcard.ru'), \
            'Не произошёл переход на страницу halalcard.ru'
        take_screenshot(appium_driver, test_name='test_go_to_halal_card', folder_name='services_page',
                        screenshot_name='screenshot_after_check_current_url')
