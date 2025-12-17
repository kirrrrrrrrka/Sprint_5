from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        """Открыть страницу"""
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        """Найти элемент на странице"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        """Кликнуть по элементу"""
        element = self.find_element(locator)
        element.click()

    def input_text(self, locator, text):
        """Ввести текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator, timeout=5):
        """Проверить, что элемент видим"""
        try:
            self.find_element(locator, timeout)
            return True
        except:
            return False

    def get_element_text(self, locator):
        """Получить текст элемента"""
        element = self.find_element(locator)
        return element.text

    def wait_for_url(self, url, timeout=10):
        """Ожидать определенный URL"""
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """Ожидать, пока элемент станет кликабельным"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )