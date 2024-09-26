from selenium.common import TimeoutException
from utils.appium_helpers import AppiumHelpers


# Страница с оплатой подписки
class SubscriptionPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def go_to_rm_plus(self, duration):
        self._helpers.wait_and_click('//android.widget.Button[@text="1 месяц 3 руб. в день"]')

    def go_to_rm_vip(self):
        self._helpers.wait_and_click('(//android.widget.Button[@text="Оформить сейчас"])[2]')

    def set_fio(self, fio):
        (self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View'
            '/android.view.View/android.view.View/android.view.View/android.view.View/android.view'
            '.View/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.view.View/android.view.View/android'
            '.view.View[1]/android.view.View/android.view.View/android.widget.EditText')
         .send_keys(fio))

    def set_email(self, email):
        (self._helpers.wait_for_element(
            '//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view.View'
            '/android.view.View/android.view.View/android.view.View/android.view.View/android.view'
            '.View/android.view.View/android.view.View['
            '2]/android.view.View/android.view.View/android.view.View/android.view.View/android'
            '.view.View[2]/android.view.View/android.view.View/android.widget.EditText')
         .send_keys(email))

    def click_continue_btn(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Продолжить"]')

    def verify_payment_page_loaded(self, timeout=20):
        """Проверяет, что страница оплаты загружена."""
        try:
            payment_page_identifier = self._helpers.wait_for_element('//android.view.View[@text="ОПЛАТА"]',
                                                                     timeout=timeout)
            return payment_page_identifier is not None
        except TimeoutException:
            return False
