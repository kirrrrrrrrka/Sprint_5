from pages.base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/login"

    def open(self):
        """Открыть страницу авторизации"""
        self.driver.get(self.url)

    def is_title_visible(self):
        """Проверить видимость заголовка 'Вход'"""
        return self.is_element_visible(LoginPageLocators.TITLE)

    def login(self, email, password):
        """Выполнить вход"""
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def click_register_link(self):
        """Кликнуть по ссылке 'Зарегистрироваться'"""
        self.click_element(LoginPageLocators.REGISTER_LINK)

    def click_forgot_password_link(self):
        """Кликнуть по ссылке 'Восстановить пароль'"""
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def is_login_page(self):
        """Проверить, что находимся на странице логина"""
        return self.is_element_visible(LoginPageLocators.TITLE)