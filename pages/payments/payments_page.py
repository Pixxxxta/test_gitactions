from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.appium_helpers import AppiumHelpers
import os
from selenium.common import NoSuchElementException, TimeoutException

class PaymentsPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def go_to_payment_patent(self):
        """
        Функция для перехода в оплату патента
        """

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Оплата патента"]'))
        ).click()

    def go_to_payment_state_duty(self):
        """
        Функция для перехода в оплату госпошлины
        """

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Оплата госпошлины"]'))
        ).click()

    def go_to_fines_mvd(self):
        """
        Функция для перехода в проверку штрафов МВД
        """

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Штрафы МВД"]'))
        ).click()

    def go_to_fines_gibdd(self):
        """
        Функция для перехода в проверку штрафов ГИБДД
        """

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Штрафы ГИБДД"]'))
        ).click()

    def go_to_court_debts(self):
        """
        Функция для перехода в проверку судебных задолженностей
        """

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Судебные задолженности"]'))
        ).click()

    def go_to_payment_taxes(self):
        """
        Функция для перехода в проверку оплаты налогов
        """
        screenshot_path = os.path.abspath(os.path.join(os.getcwd(), 'artifacts', 'screenshot_taxes.png'))
        self._driver.save_screenshot(screenshot_path)
        try:
            WebDriverWait(self._driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@text='Оплата налогов']"))
            ).click()
        except TimeoutException:
            screenshot_path = os.path.abspath(os.path.join(os.getcwd(), 'artifacts', 'screenshot_failed_taxes.png'))
            self._driver.save_screenshot(screenshot_path)
            raise TimeoutException(f"Элемент c текстом Оплата налогов не найден")
        print("Перешли в оплату налогов")
