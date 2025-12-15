from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import RegisterPageLocators


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://stellarburgers.education-services.ru/register"
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    def get_element_text(self, locator):
        try:
            element = self.find_element(locator)
            return element.text
        except:
            return None

    # методы для страницы регистрации
    def is_title_visible(self):
        return self.is_element_visible(RegisterPageLocators.TITLE)

    #"Выполнить регистрацию"
    def register(self, name, email, password):
        self.input_text(RegisterPageLocators.NAME_INPUT, name)
        self.input_text(RegisterPageLocators.EMAIL_INPUT, email)
        self.input_text(RegisterPageLocators.PASSWORD_INPUT, password)
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)

    def click_login_link(self):
        self.click_element(RegisterPageLocators.LOGIN_LINK)

    def is_password_error_visible(self):
        return self.is_element_visible(RegisterPageLocators.PASSWORD_ERROR, timeout=2)

    def get_password_error_text(self):
        return self.get_element_text(RegisterPageLocators.PASSWORD_ERROR)