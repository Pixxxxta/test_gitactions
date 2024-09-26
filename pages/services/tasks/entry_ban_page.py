import time

from selenium.common import TimeoutException
from utils.appium_helpers import AppiumHelpers


# Страница с проверкой мед книжки
class EntryBanPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def close_rm_window(self):
        self._helpers.wait_and_click(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android'
            '.view.View/android.view.View/android.view.View/android.view.View/android.view.View'
            '/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.widget.Button[1]')

    def click_back_btn(self):
        self._driver.press_keycode(4)

    def set_last_name(self, last_name):
        self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android'
            '.view.View/android.view.View/android.view.View/android.view.View/android.view.View'
            '/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.view.View/android.view.View/android'
            '.widget.EditText[1]').send_keys(last_name)

    def set_name(self, name):
        self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View'
            '/android.view.View/android.view.View/android.view.View/android.view.View/android.view'
            '.View/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.view.View/android.view.View/android'
            '.widget.EditText[2]').send_keys(name)

    def choose_gender(self, gender):
        self._helpers.wait_and_click(f'//android.view.View[@text="{gender}"]')

    def set_date(self, date):
        self._helpers.wait_and_click('(//android.widget.EditText[@text="__.__.____"])[1]')
        time.sleep(1)
        self._helpers.adb_input_text(date)
        time.sleep(1)
        self.click_back_btn()

    def choose_citizenship(self, citizenship):
        self._helpers.wait_and_click('(//android.view.View[@text="Узбекистан"])[1]')
        time.sleep(1)
        self._helpers.wait_and_click(
            f'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="{citizenship}"]')

    def choose_doc_type(self, doc_type):
        self._helpers.wait_and_click('//android.view.View[@text="Национальный паспорт"]')
        time.sleep(1)
        self._helpers.wait_and_click(
            f'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="{doc_type}"]')

    def choose_doc_country(self, doc_country):
        self._helpers.wait_and_click('//android.view.View[@text="Узбекистан"]')
        time.sleep(1)
        self._helpers.wait_and_click(
            f'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="{doc_country}"]')

    def set_doc_num(self, doc_num):
        self._helpers.wait_and_click(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view.View'
            '/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view'
            '.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget'
            '.EditText[4]')
        time.sleep(1)
        self._helpers.adb_input_text(doc_num)
        time.sleep(1)
        self.click_back_btn()

    def set_doc_duration_date(self, duration_date):
        self._helpers.wait_and_click('(//android.widget.EditText[@text="__.__.____"])')
        time.sleep(1)
        self._helpers.adb_input_text(duration_date)
        time.sleep(1)
        self.click_back_btn()

    def click_check_btn(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Проверить"]')

    def verify_have_entry_ban(self, timeout=20):
        """Проверяет, что обнаружен запрет на въезд"""
        try:
            med_book_data = self._helpers.wait_for_element(
                '//android.widget.TextView[@text="ОБНАРУЖЕН ЗАПРЕТ НА ВЪЕЗД"]', timeout=timeout)
            return med_book_data is not None
        except TimeoutException:
            return False

    def verify_no_entry_ban(self, timeout=20):
        """Проверяет, что страница оплаты загружена."""
        try:
            med_book_data = self._helpers.wait_for_element(
                '//android.widget.TextView[@text="ОБНАРУЖЕН ЗАПРЕТ НА ВЪЕЗД"]',
                timeout=timeout)
            return med_book_data is not None
        except TimeoutException:
            return False
