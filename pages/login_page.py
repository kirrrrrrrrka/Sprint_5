from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://stellarburgers.education-services.ru/login"
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

    def is_element_visible(self, locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False

    def wait_for_url(self, url):
        return self.wait.until(EC.url_to_be(url))

    # методыы для страницы авторизации
    def is_title_visible(self):
        return self.is_element_visible(LoginPageLocators.TITLE)

    def login(self, email, password):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def click_register_link(self):
        self.click_element(LoginPageLocators.REGISTER_LINK)

    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)