from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import ProfilePageLocators


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://stellarburgers.education-services.ru/account/profile"
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

    def wait_for_url(self, url):
        return self.wait.until(EC.url_to_be(url))

    # методы для страницы профиля
    def is_profile_visible(self):
        return self.is_element_visible(ProfilePageLocators.PROFILE_LINK)
    # кликн по кнопке 'Выход'
    def click_logout(self):
        
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    def wait_for_profile_page(self):
        self.wait_for_url("https://stellarburgers.education-services.ru/account/profile")
        self.is_profile_visible()