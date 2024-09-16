import time

from selenium.common import TimeoutException
from utils.appium_helpers import AppiumHelpers


# Страница с проверкой РВП и ВНЖ
class StayControlCalculatorPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def close_info_page(self):
        self._helpers.wait_and_click('//*[@text="Понятно"]')

    def set_first_entry_date(self, date):
        self._helpers.wait_and_click('//android.view.View[@resource-id="situation_iframe"]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText', timeout=5)
        self._helpers.adb_input_text(date)

    def click_ready_btn(self):
        self._helpers.wait_and_click('//*[@text="Готово"]')

    def verify_end_date_of_stay(self, end_date):
        end_date_element = self._helpers.wait_for_element(f'//*[@text="{end_date}"]')
        return end_date_element is not None

    def verify_period_of_stay(self, period_of_stay):
        end_date_element = self._helpers.wait_for_element(f'//*[@text="{period_of_stay}"]')
        return end_date_element is not None

    def click_add_period_btn(self):
        self._helpers.wait_and_click('//*[@text="Добавить период пребывания +"]')

