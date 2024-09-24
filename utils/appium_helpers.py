from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AppiumHelpers:
    def __init__(self, driver):
        self._driver = driver

    def find_all_textview(self, timeout=60):
        """Находит все элементы EditText на странице и возвращает их списком."""
        try:
            # Ожидаем загрузки всех элементов EditText на экране
            WebDriverWait(self._driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, '//android.widget.TextView'))
            )
            # Находим и возвращаем все элементы EditText
            return self._driver.find_elements(By.XPATH, '//android.widget.TextView')
        except TimeoutException:
            raise TimeoutException("Не удалось найти элементы TextView на экране.")

    def find_all_edittexts(self, timeout=60):
        """Находит все элементы EditText на странице и возвращает их списком."""
        try:
            # Ожидаем загрузки всех элементов EditText на экране
            WebDriverWait(self._driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, '//android.widget.EditText'))
            )
            # Находим и возвращаем все элементы EditText
            return self._driver.find_elements(By.XPATH, '//android.widget.EditText')
        except TimeoutException:
            raise TimeoutException("Не удалось найти элементы EditText на экране.")

    def wait_for_element(self, value, by=By.XPATH, timeout=60):
        """Ожидает появления элемента на странице."""
        try:
            return WebDriverWait(self._driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, value))
            )
        except TimeoutException:
            raise TimeoutException(f"Элемент с локатором '{value}' не найден")

    def wait_and_click(self, value, by=By.XPATH, timeout=60):
        """Ожидает появления элемента и кликает на него."""
        try:
            element = self.wait_for_element(value, timeout)
            WebDriverWait(self._driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, value))
            )
            element.click()
        except TimeoutException:
            raise TimeoutException(f"Элемент с локатором '{value}' не найден или не стал кликабельным.")

    def swipe_down(self, duration=1000):
        """Прокручивает экран вниз."""
        size = self._driver.get_window_size()
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.2
        start_x = size['width'] / 2
        self._driver.swipe(start_x, start_y, start_x, end_y, duration)

    def swipe_up(self, duration=1000):
        """Прокручивает экран вверх."""
        size = self._driver.get_window_size()
        start_y = size['height'] * 0.2
        end_y = size['height'] * 0.8
        start_x = size['width'] / 2
        self._driver.swipe(start_x, start_y, start_x, end_y, duration)

    def adb_input_text(self, text):
        """Использует команду ADB для ввода текста."""
        self._driver.execute_script("mobile: shell", {
            "command": "input",
            "args": ["text", text]
        })

    def slow_type(self, xpath, text, delay=0.1):
        """Ввод текста по одному символу с задержкой."""
        element = self._driver.find_element_by_xpath(xpath)
        element.click()
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    def is_element_present(self, value, by=By.XPATH, timeout=60):
        try:
            saved_doc = self.wait_for_element(value=value, by=by, timeout=timeout)
            return saved_doc is not None
        except TimeoutException:
            return False

    def find_element_with_scroll(self, xpath, max_swipes=15, timeout=30):
        """Прокручивает экран, пока не найдет элемент с заданным xpath или не выполнит все прокруты."""
        for _ in range(max_swipes):
            try:
                element = self.wait_for_element(xpath, timeout=timeout)
                return element
            except:
                self.swipe_down()
        raise Exception(f"Element with xpath {xpath} not found after {max_swipes} swipes")
