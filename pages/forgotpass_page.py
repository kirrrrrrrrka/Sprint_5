from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import ForgotPasswordPageLocators


class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://stellarburgers.education-services.ru/forgot-password"
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def is_element_visible(self, locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False

    # методы для страницы восстановления пароля
    def is_title_visible(self):
        return self.is_element_visible(ForgotPasswordPageLocators.TITLE)

    def click_login_link(self):
        self.click_element(ForgotPasswordPageLocators.LOGIN_LINK)