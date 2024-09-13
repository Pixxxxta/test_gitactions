from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.appium_helpers import AppiumHelpers
import os


class PaymentsPage:
    def __init__(self, driver):
        self._driver = driver
        self._helpers = AppiumHelpers(driver)

    def go_to_payment_patent(self):
        """
        Функция для перехода в оплату патента
        """

        WebDriverWait(self._driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@text="Оплата патента"]'))
        ).click()

    def go_to_payment_state_duty(self):
        """
        Функция для перехода в оплату госпошлины
        """

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@text="Оплата госпошлины"]'))
        ).click()

    def go_to_fines_mvd(self):
        """
        Функция для перехода в проверку штрафов МВД
        """

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@text="Штрафы МВД"]'))
        ).click()

    def go_to_fines_gibdd(self):
        """
        Функция для перехода в проверку штрафов ГИБДД
        """

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@text="Штрафы ГИБДД"]'))
        ).click()

    def go_to_court_debts(self):
        """
        Функция для перехода в проверку судебных задолженностей
        """

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@text="Судебные задолженности"]'))
        ).click()

    def go_to_payment_taxes(self):
        """
        Функция для перехода в проверку оплаты налогов
        """
        WebDriverWait(self._driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@text="Оплата налогов"]'))
        ).click()
        screenshot_path = os.path.abspath(os.path.join(os.getcwd(), 'artifacts', 'screenshot_go_to_taxes.png'))
        self._driver.save_screenshot(screenshot_path)
