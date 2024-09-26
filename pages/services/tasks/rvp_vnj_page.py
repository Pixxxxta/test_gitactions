import time

from selenium.common import TimeoutException
from utils.appium_helpers import AppiumHelpers


# Страница с проверкой РВП и ВНЖ
class RvpVnjPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def find_element_with_scroll(self, xpath, max_swipes=50, timeout=10):
        """Прокручивает экран, пока не найдет элемент с заданным xpath или не выполнит все прокруты."""
        for _ in range(max_swipes):
            try:
                element = self._helpers.wait_for_element(xpath, timeout=timeout)
                return element
            except:
                self._helpers.swipe_down()
        raise Exception(f"Element with xpath {xpath} not found after {max_swipes} swipes")

    def close_rm_window(self):
        self._helpers.wait_and_click('//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view'
                                     '.View/android'
                                     '.view.View/android.view.View/android.view.View/android.view.View/android.view'
                                     '.View'
                                     '/android.view.View/android.view.View['
                                     '2]/android.view.View/android.view.View/android.view.View/android.view.View['
                                     '2]/android.view.View/android.view.View/android.widget.Button[1]')

    def click_check_btn(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Проверить"]')

    def choose_check_type(self, check_type):
        self._helpers.wait_and_click(f'//android.view.View[@text="{check_type}"]')

    def click_back_btn(self):
        self._driver.press_keycode(4)

    def set_date(self, date):
        self._helpers.wait_and_click(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view.View'
            '/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view'
            '.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View['
            '4]/android.view.View/android.view.View/android.widget.EditText')
        self._helpers.adb_input_text(date)
        time.sleep(1)
        self.click_back_btn()
        time.sleep(1)

    def set_passport(self, passport_data):
        self._helpers.wait_and_click(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view.View'
            '/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view'
            '.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View['
            '5]/android.view.View/android.view.View/android.widget.EditText')
        self._helpers.adb_input_text(passport_data)
        time.sleep(1)
        self.click_back_btn()
        time.sleep(1)

    def choose_region(self, region, timeout=10):
        self._helpers.wait_and_click('//android.view.View[@text="Не выбрано"]')
        time.sleep(1)
        self.find_element_with_scroll(
            f'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="{region}"]',
            timeout=timeout).click()

    def verify_rvp_found(self, timeout=20):
        """Проверяет, что выдан вид на жительство"""
        try:
            med_book_data = self._helpers.wait_for_element('//android.widget.TextView[@text="выдан вид на жительство"]',
                                                           timeout=timeout)
            return med_book_data is not None
        except TimeoutException:
            return False

    def click_new_capcha_btn(self):
        try:
            self._helpers.wait_and_click('//*[@text="Загрузить другое изображение"]')
        except:
            raise TimeoutException('Кнопка для обновления капчи не появилась на экране или не стала кликабельной')



