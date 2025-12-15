import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.forgotpass_page import ForgotPasswordPage
from generators import generate_email, generate_name, generate_password


class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.register_page = RegisterPage(driver)
        self.forgot_password_page = ForgotPasswordPage(driver)
        
        # Регистрируем пользователя для тестов входа
        self.test_name = generate_name()
        self.test_email = generate_email()
        self.test_password = generate_password(8)
        
        self.register_page.open()
        self.register_page.register(self.test_name, self.test_email, self.test_password)
        self.login_page.wait_for_url("https://stellarburgers.education-services.ru/login")

    def test_login_from_main_page_login_button(self):
        """Тест входа через кнопку 'Войти в аккаунт' на главной"""
        # Открываем главную страницу
        self.main_page.open()
        
        # Кликаем по кнопке "Войти в аккаунт"
        self.main_page.click_login_button()
        
        # Выполняем вход
        self.login_page.login(self.test_email, self.test_password)
        
        # Проверяем, что перешли на главную страницу
        assert self.main_page.is_constructor_title_visible()

    def test_login_from_account_button(self):
        """Тест входа через кнопку 'Личный кабинет'"""
        # Открываем главную страницу
        self.main_page.open()
        
        # Кликаем по кнопке "Личный кабинет" (без авторизации)
        self.main_page.click_account_button()
        
        # Выполняем вход
        self.login_page.login(self.test_email, self.test_password)
        
        # Проверяем, что перешли на главную страницу
        assert self.main_page.is_constructor_title_visible()

    def test_login_from_register_page(self):
        """Тест входа через кнопку в форме регистрации"""
        # Открываем страницу регистрации
        self.register_page.open()
        
        # Кликаем по ссылке "Войти" на странице регистрации
        self.register_page.click_login_link()
        
        # Выполняем вход
        self.login_page.login(self.test_email, self.test_password)
        
        # Проверяем, что перешли на главную страницу
        assert self.main_page.is_constructor_title_visible()

    def test_login_from_forgot_password_page(self):
        """Тест входа через кнопку в форме восстановления пароля"""
        # Открываем страницу восстановления пароля
        self.forgot_password_page.open()
        
        # Кликаем по ссылке "Войти" на странице восстановления пароля
        self.forgot_password_page.click_login_link()
        
        # Выполняем вход
        self.login_page.login(self.test_email, self.test_password)
        
        # Проверяем, что перешли на главную страницу
        assert self.main_page.is_constructor_title_visible()