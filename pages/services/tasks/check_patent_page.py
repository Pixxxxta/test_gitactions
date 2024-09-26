from utils.appium_helpers import AppiumHelpers


# Страница с проверкой патента
class CheckPatentPage:
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

    def click_check_btn(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Проверить"]')

    def set_patent_data(self, patent_data):
        self._helpers.wait_for_element('//android.widget.EditText[@text="__ __________"]').send_keys(patent_data)

    def set_blank_data(self, blank_data):
        self._helpers.wait_for_element('//android.widget.EditText[@text="__ _______"]').send_keys(blank_data)

    def set_passport(self, passport_data):
        self._helpers.wait_for_element('//android.webkit.WebView[@text="РосМигрант"]/android.view.View/android.view'
                                       '.View/android.view.View/android.view.View/android.view.View/android.view.View'
                                       '/android.view.View/android.view.View/android.view.View['
                                       '2]/android.view.View/android.view.View/android.view.View/android.view.View'
                                       '/android.widget.EditText[3]').send_keys(passport_data)

    def press_back_btn(self):
        self._driver.press_keycode(4)
