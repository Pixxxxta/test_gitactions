import time

import pytest
from appium import webdriver
from utils.config import emulator_name, android_version
from appium.options.android import UiAutomator2Options
from pages.start_page import StartPage
import os


@pytest.fixture(scope="function")
def appium_driver(request):
    # app-debug.apk - последняя версия дева
    # myapp.apk - последняя версия прода
    apk_path = os.path.abspath(
        os.path.join(os.getcwd(), 'artifacts', 'app', 'app-debug.apk'))

    desired_caps = {
        'platformName': 'Android',
        'deviceName': emulator_name,
        'platformVersion': android_version,
        'app': apk_path,
        'appPackage': 'rosmigrant.online.app',
        'appActivity': '.MainActivity',
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub',
                              options=UiAutomator2Options().load_capabilities(desired_caps))

    start_page = StartPage(driver)
    start_page.select_language()

    yield driver
    driver.quit()


@pytest.fixture
def uninstall_app(appium_driver):
    def _uninstall():
        appium_driver.remove_app("rosmigrant.online.app")

    return _uninstall

