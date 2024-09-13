import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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
            "Узбекский": '//*[@text="Ўзбек"]',
            "Таджикский": '//*[@text="Тоҷикӣ"]',
            "Кыргызский": '//*[@text="Кыргыз"]'
        }

        xpath = languages_xpath.get(language)
        print(xpath)
        if xpath:
            try:
                WebDriverWait(self._driver, 60).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                ).click()
                time.sleep(5)
            except TimeoutException:
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
        try:
            self._click_element_by_xpath('//*[@text="Лента"]')
        except TimeoutException:
            raise TimeoutException("Не удалось перейти на страницу с новостями")

    def go_to_payments(self):
        """
        Функция для перехода на страницу с платежами
        """
        try:
            self._click_element_by_xpath("//*[@text='Платежи']")
        except TimeoutException:
            raise TimeoutException("Не удалось перейти на страницу с платежами")

    def go_to_tasks(self):
        """
        Функция для перехода на страницу с задачами
        """
        try:
            self._click_element_by_xpath('//*[@text="Задачи"]')
        except TimeoutException:
            raise TimeoutException("Не удалось перейти на страницу с задачами")

    def go_to_account(self):
        """
        Функция для перехода на страницу с аккаунтом
        """
        try:
            self._click_element_by_xpath('//*[@text="Аккаунт"]')
        except TimeoutException:
            raise TimeoutException("Не удалось перейти на страницу с аккаунтом")

    def _click_element_by_xpath(self, xpath):
        """
        Внутренняя функция для клика по элементу по XPath
        """
        try:
            WebDriverWait(self._driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            ).click()
        except TimeoutException:
            raise TimeoutException(f"Элемент по XPath '{xpath}' не был найден или не стал кликабельным.")

    def go_to_subscription(self):
        self._click_element_by_xpath('//android.widget.Button[@text="Оформить сейчас"]')
