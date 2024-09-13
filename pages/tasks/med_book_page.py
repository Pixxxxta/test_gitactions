import time

from selenium.common import TimeoutException
from utils.appium_helpers import AppiumHelpers


# Страница с проверкой мед книжки
class MedBookPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def close_rm_window(self):
        self._helpers.wait_and_click('//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view'
                                     '.View/android'
                                     '.view.View/android.view.View/android.view.View/android.view.View/android.view'
                                     '.View'
                                     '/android.view.View/android.view.View['
                                     '2]/android.view.View/android.view.View/android.view.View/android.view.View['
                                     '2]/android.view.View/android.view.View/android.widget.Button[1]')

    def set_med_book_data(self, data):
        time.sleep(1)
        self._helpers.wait_and_click('//android.widget.EditText')
        time.sleep(1)
        self._helpers.adb_input_text(data)

    def click_check_btn(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Проверить"]')

    def verify_med_book_data(self, timeout=20):
        """Проверяет, что страница оплаты загружена."""
        try:
            med_book_data = self._helpers.wait_for_element('//android.widget.Image[@text="success"]', timeout=timeout)
            return med_book_data is not None
        except TimeoutException:
            return False

    def verify_med_book_data_not_found(self, timeout=20):
        """Проверяет, что страница оплаты загружена."""
        try:
            med_book_data = self._helpers.wait_for_element('//android.widget.Image[@text="error"]', timeout=timeout)
            return med_book_data is not None
        except TimeoutException:
            return False

    def scroll_d(self):
        self._helpers.swipe_down()

