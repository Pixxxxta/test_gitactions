from pages.start_page import StartPage
from pages.tasks.tasks_page import TasksPage
from pages.tasks.subscription_page import SubscriptionPage


class TestSubscription:
    def test_rm_plus(self, appium_driver):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)
        # Инициализация страницы с подпиской
        subscription_page = SubscriptionPage(appium_driver)

        # Переход на страницу с подпиской с главного экрана
        start_page.go_to_subscription()

        subscription_page.go_to_rm_plus()
        subscription_page.set_fio('Джорджо Джавани')
        subscription_page.set_email('123@123.com')
        subscription_page.click_continue_btn()

        assert subscription_page.verify_payment_page_loaded(), 'Страница с оплатой не загружена'

    def test_rm_vip(self, appium_driver):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)
        # Инициализация страницы с подпиской
        subscription_page = SubscriptionPage(appium_driver)

        # Переход на страницу с подпиской с главного экрана
        start_page.go_to_subscription()

        subscription_page.go_to_rm_vip()
        subscription_page.set_fio('Джорджо Джавани')
        subscription_page.set_email('123@123.com')
        subscription_page.click_continue_btn()

        assert subscription_page.verify_payment_page_loaded(), 'Страница с оплатой не загружена'
