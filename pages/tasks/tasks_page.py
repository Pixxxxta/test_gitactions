import time

from selenium.common import TimeoutException
from utils.appium_helpers import AppiumHelpers


# Страница с задачами
class TasksPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def go_to_resume_page(self):
        time.sleep(1)
        self._helpers.wait_and_click('//android.widget.Button[@text="Создать резюме"]')

    def go_to_naimix(self):
        time.sleep(1)
        self._helpers.wait_and_click('//android.widget.Button[@text="Зарегистрироваться"]')

    def go_to_halal_card(self):
        self._helpers.swipe_down()
        time.sleep(1)
        self._helpers.wait_and_click('//android.widget.Button[@text="Подробнее"]')

    def go_to_b24(self):
        time.sleep(1)
        self._helpers.wait_and_click('//android.widget.Button[@text="Записаться"]')

    def go_to_med_book(self):
        for i in range(10):
            print(f'Итерация - {i}')
            element = self._helpers.is_element_present(value='//*[@text="Проверить мед.книжку"]')
            print(element)
            if element:
                return True
            else:
                self._helpers.swipe_down()
                time.sleep(2)
        return False
        # self._helpers.find_element_with_scroll(xpath='//*[@text="Проверить мед.книжку"]')
        # self._helpers.wait_and_click('//*[@text="Проверить"]')

    def click_med_book_btn(self):
        self._helpers.wait_and_click('//*[@text="Проверить"]')

    def check_current_url(self, current_url):
        """Проверяет, что страница с нужным url загружена"""
        try:
            site_page = self._helpers.wait_for_element('//android.widget.TextView['
                                                       '@resource-id="com.android.chrome:id/url_bar"]')
            return current_url == site_page.text
        except TimeoutException:
            return False

    def go_to_check_patent(self):
        time.sleep(1)
        self.scroll_down_page()
        self._helpers.wait_and_click('(//android.widget.Button[@text="Проверить"])[2]')

    def go_to_check_rvp_vnj(self):
        time.sleep(1)
        self.scroll_down_page()
        self._helpers.wait_and_click('(//android.widget.Button[@text="Проверить"])[3]')

    def go_to_check_entry_ban(self):
        time.sleep(1)
        self.scroll_down_page()
        self._helpers.wait_and_click('(//android.widget.Button[@text="Проверить"])[1]')

    def scroll_down_page(self):
        for i in range(5):
            self._helpers.swipe_down()
        time.sleep(1)
