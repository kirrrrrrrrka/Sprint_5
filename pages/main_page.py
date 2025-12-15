from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, ConstructorPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://stellarburgers.education-services.ru/"
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

    # Методы для главной страницы
    def click_login_button(self):
        self.click_element(MainPageLocators.LOGIN_BUTTON)

    def click_account_button(self):
        self.click_element(MainPageLocators.ACCOUNT_BUTTON)

    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_logo(self):
        self.click_element(MainPageLocators.LOGO)

    def is_constructor_title_visible(self):
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_TITLE)

    def click_buns_section(self):
        self.click_element(ConstructorPageLocators.BUNS_SECTION)

    def click_sauces_section(self):
        self.click_element(ConstructorPageLocators.SAUCES_SECTION)

    def click_fillings_section(self):
        self.click_element(ConstructorPageLocators.FILLINGS_SECTION)

     #выбран раздел 'Булки'
    def is_buns_selected(self):
        return self.is_element_visible(ConstructorPageLocators.BUNS_SELECTED)
    
    #выбран раздел 'Соусы'
    def is_sauces_selected(self):
        return self.is_element_visible(ConstructorPageLocators.SAUCES_SELECTED)
    
    #выбран раздел 'Начинки'
    def is_fillings_selected(self):
        return self.is_element_visible(ConstructorPageLocators.FILLINGS_SELECTED)