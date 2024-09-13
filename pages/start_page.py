import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class StartPage:
    def __init__(self, driver):
        self._driver = driver

    def select_language(self, language='Русский'):
        """
        Выбор языка

        :param language: Язык, который нужно выбрать. Допустимые значения: Русский, Узбекский, Таджикский, Кыргызский
        :return: None
        """
        languages_xpath = {
            "Русский": "//*[@text='Русский']",
            "Узбекский": '//android.widget.TextView[@text="Ўзбек"]',
            "Таджикский": '//android.widget.TextView[@text="Тоҷикӣ"]',
            "Кыргызский": '//android.widget.TextView[@text="Кыргыз"]'
        }

        xpath = languages_xpath.get(language)
        print(xpath)
        if xpath:
            try:
                time.sleep(40)
                print("Language select check before click")
                screenshot_path = os.path.abspath(os.path.join(os.getcwd(), 'artifacts', 'screenshot_language_error.png'))
                self._driver.save_screenshot(screenshot_path)
                print(f"Скриншот сохранён: {screenshot_path}")
                print(f"Current activity: {self._driver.current_activity}")
                print(f"Page source: {self._driver.page_source}")
                WebDriverWait(self._driver, 60).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                ).click()
            except TimeoutException:
                print("Language select check after click")
                screenshot_path = os.path.abspath(
                    os.path.join(os.getcwd(), 'artifacts', 'screenshot_language_error.png'))
                self._driver.save_screenshot(screenshot_path)
                print(f"Скриншот сохранён: {screenshot_path}")
                raise NoSuchElementException(f"Элемент с языком '{language}' не найден.")
        else:
            raise ValueError("Недопустимое значение языка. Допустимые значения: Русский, Узбекский, Таджикский, "
                             "Кыргызский")

    def is_language_selected(self, language='Русский'):
        """
        Проверка выбранного языка

        :param language: Выбранный язык. Допустимые значения: Русский, Узбекский, Таджикский, Кыргызский
        :return: True, если текст на главное странице соответствует выбранному языку, False в противном случае
        """
        languages_xpath = {
            "Русский": '//android.view.View[@text="Лента новостей"]',
            "Узбекский": '//android.view.View[@text="Янгиликлар лентаси"]',
            "Таджикский": '///android.view.View[@text="Хатти ахбор"]',
            "Кыргызский": '//android.view.View[@text="Жаңылыктар түрмөгү"]'
        }

        xpath = languages_xpath.get(language)
        if xpath:
            try:
                self._driver.find_element(By.XPATH, xpath)
                return True
            except NoSuchElementException:
                return False
        else:
            raise ValueError("Недопустимое значение языка. Допустимые значения: Русский, Узбекский, Таджикский, "
                             "Кыргызский")

    def go_to_news(self):
        """
        Функция для перехода на страницу с новостями
        """
        self._click_element_by_xpath('//android.widget.TextView[@text="Лента"]')

    def go_to_payments(self):
        """
        Функция для перехода на страницу с платежами
        """
        time.sleep(10)
        screenshot_path = os.path.abspath(os.path.join(os.getcwd(), 'artifacts', 'screenshot_payment.png'))
        self._driver.save_screenshot(screenshot_path)
        self._click_element_by_xpath("//*[@text='Платежи']")
        print("Клик в платежи")

    def go_to_tasks(self):
        """
        Функция для перехода на страницу с задачами
        """
        self._click_element_by_xpath('//android.widget.TextView[@text="Задачи"]')

    def go_to_account(self):
        """
        Функция для перехода на страницу с аккаунтом
        """
        self._click_element_by_xpath('//android.widget.TextView[@text="Аккаунт"]')

    def _click_element_by_xpath(self, xpath):
        """
        Внутренняя функция для клика по элементу по XPath
        """
        try:
            WebDriverWait(self._driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            ).click()
            time.sleep(5)
            screenshot_path = os.path.abspath(os.path.join(os.getcwd(), 'artifacts', f'screenshot_{xpath}.png'))
            self._driver.save_screenshot(screenshot_path)
        except TimeoutException:
            raise TimeoutException(f"Элемент по XPath '{xpath}' не был найден или не стал кликабельным.")

    def go_to_subscription(self):
        self._click_element_by_xpath('//android.widget.Button[@text="Оформить сейчас"]')