from pages.base_page import BasePage
from locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/forgot-password"

    def open(self):
        """Открыть страницу восстановления пароля"""
        self.driver.get(self.url)

    def is_title_visible(self):
        """Проверить видимость заголовка 'Восстановление пароля'"""
        return self.is_element_visible(ForgotPasswordPageLocators.TITLE)

    def click_login_link(self):
        """Кликнуть по ссылке 'Войти'"""
        self.click_element(ForgotPasswordPageLocators.LOGIN_LINK)