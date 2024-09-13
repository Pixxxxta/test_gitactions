import time

from selenium.common import TimeoutException
from utils.appium_helpers import AppiumHelpers


# Страница с оплатой подписки
class ResumePage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def set_fio(self, fio):
        self._helpers.wait_and_click(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android.view.View'
            '/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view'
            '.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View'
            '/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.EditText')

        (self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View'
            '/android.view.View/android.view.View/android.view.View/android.view.View/android.view'
            '.View/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.view.View/android.view.View/android'
            '.view.View/android.view.View/android.view.View['
            '1]/android.view.View/android.view.View/android.widget.EditText')
         .send_keys(fio))

    def choose_gender(self, gender):
        self._helpers.wait_and_click(f'//android.view.View[@text="{gender}"]')

    def set_age(self, age):
        (self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View'
            '/android.view.View/android.view.View/android.view.View/android.view.View/android.view'
            '.View/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.view.View/android.view.View/android'
            '.view.View/android.view.View['
            '4]/android.view.View/android.view.View/android.widget.EditText')
         .send_keys(age))

    def choose_citizenship(self, citizenship):
        self._helpers.wait_and_click('//android.view.View[@text="Россия"]')
        self._helpers.wait_and_click(
            f'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="{citizenship}"]')

    def choose_city(self, city):
        self._helpers.wait_and_click(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android'
            '.view.View/android.view.View/android.view.View/android.view.View/android.view.View'
            '/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view'
            '.View/android.view.View/android.view.View['
            '6]/android.view.View/android.view.View/android.widget.EditText')
        time.sleep(1)
        self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View'
            '/android.view.View/android.view.View/android.view.View/android.view.View/android.view'
            '.View/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.widget.EditText').send_keys(city)
        time.sleep(1)
        self._helpers.wait_and_click(f'//android.widget.TextView[@text="{city}"]')

    def click_continue_btn(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Далее"]')

    def click_save_btn(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Сохранить"]')

    def choose_type_of_employment(self, employment):
        for emp in employment:
            self._helpers.wait_and_click(f'//android.widget.CheckBox[@text="{emp}"]')

    def choose_post(self, post, type='Из списка'):
        # TODO добавить ручной ввод должности
        self._helpers.wait_and_click(f'//android.view.View[@text="{post}"]')

    def choose_education(self, education):
        self._helpers.wait_and_click(f'//android.view.View[@text="{education}"]')

    def choose_work_experience(self, type, experience=None):
        self._helpers.wait_and_click(f'//android.view.View[@text="{type}"]')
        if experience is not None:
            for exp in experience:
                self._helpers.wait_and_click(f'//android.view.View[@text="{exp}"]')

    def set_phone_number(self, number):
        self._helpers.wait_and_click(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View/android'
            '.view.View/android.view.View/android.view.View/android.view.View/android.view.View'
            '/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view'
            '.View/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.widget.EditText')

    def set_email(self, email):
        self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View'
            '/android.view.View/android.view.View/android.view.View/android.view.View/android.view'
            '.View/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.view.View/android.view.View/android'
            '.view.View/android.view.View['
            '3]/android.view.View/android.view.View/android.widget.EditText').send_keys(email)

    def choose_ready_for_work(self, answer):
        self._helpers.wait_and_click(f'//android.view.View[@text="{answer}"]')

    def verify_correct_resume_data(self, timeout=20):
        """Проверяет, что страница оплаты загружена."""
        try:
            payment_page_identifier = self._helpers.wait_for_element('//android.view.View[@text="ОПЛАТА"]',
                                                                     timeout=timeout)
            return payment_page_identifier is not None
        except TimeoutException:
            return False
