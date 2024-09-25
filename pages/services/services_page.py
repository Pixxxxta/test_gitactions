import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.appium_helpers import AppiumHelpers
import os


class ServicesPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def go_to_payment_patent(self):
        """
        Функция для перехода в оплату патента
        """
        self._helpers.find_element_with_scroll(xpath='//*[@text="Полезные сервисы"]', max_swipes=10, timeout=3)
        self._helpers.wait_for_element(value='//*[@text="Оплата патента"]')
        self._helpers.wait_and_click(value='//*[@text="Оплата патента"]')

    def go_to_payment_state_duty(self):
        """
        Функция для перехода в оплату госпошлины
        """

        self._helpers.find_element_with_scroll(xpath='//*[@text="Полезные сервисы"]', max_swipes=10, timeout=3)
        self._helpers.wait_for_element(value='//*[@text="Оплата госпошлины"]')
        self._helpers.wait_and_click(value='//*[@text="Оплата госпошлины"]')

    def go_to_fines_mvd(self):
        """
        Функция для перехода в проверку штрафов МВД
        """

        self._helpers.find_element_with_scroll(xpath='//*[@text="Полезные сервисы"]', max_swipes=10, timeout=3)
        self._helpers.wait_for_element(value='//*[@text="Штрафы МВД"]')
        self._helpers.wait_and_click(value='//*[@text="Штрафы МВД"]')

    def go_to_fines_gibdd(self):
        """
        Функция для перехода в проверку штрафов ГИБДД
        """

        self._helpers.find_element_with_scroll(xpath='//*[@text="Полезные сервисы"]', max_swipes=10, timeout=3)
        self._helpers.wait_for_element(value='//*[@text="Штрафы ГИБДД"]')
        self._helpers.wait_and_click(value='//*[@text="Штрафы ГИБДД"]')

    def go_to_court_debts(self):
        """
        Функция для перехода в проверку судебных задолженностей
        """

        self._helpers.find_element_with_scroll(xpath='//*[@text="Полезные сервисы"]', max_swipes=10, timeout=3)
        self._helpers.wait_for_element(value='//*[@text="Судебные задолженности"]')
        self._helpers.wait_and_click(value='//*[@text="Судебные задолженности"]')

    def go_to_payment_taxes(self):
        """
        Функция для перехода в проверку оплаты налогов
        """

        self._helpers.find_element_with_scroll(xpath='//*[@text="Полезные сервисы"]', max_swipes=10, timeout=3)
        self._helpers.wait_for_element(value='//*[@text="Оплата налогов"]')
        self._helpers.wait_and_click(value='//*[@text="Оплата налогов"]')

    def close_info_page(self):
        self._helpers.wait_and_click('//android.widget.Button[@text="Не сейчас"]')
