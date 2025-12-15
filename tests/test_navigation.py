import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from generators import generate_email, generate_name, generate_password


class TestNavigation:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.profile_page = ProfilePage(driver)
        
        # Регистрируем и логинимся один раз для всех тестов
        self.register_and_login()

    def register_and_login(self):
        """Вспомогательный метод для регистрации и входа"""
        from pages.register_page import RegisterPage
        register_page = RegisterPage(self.driver)
        
        # Генерируем тестовые данные
        self.test_name = generate_name()
        self.test_email = generate_email()
        self.test_password = generate_password(8)
        
        # Регистрируемся
        register_page.open()
        register_page.register(self.test_name, self.test_email, self.test_password)
        self.login_page.wait_for_url("https://stellarburgers.education-services.ru/login")
        
        # Логинимся
        self.login_page.login(self.test_email, self.test_password)
        self.main_page.is_constructor_title_visible()

    def test_navigate_to_account_from_main(self):
        """Тест перехода в личный кабинет с главной страницы"""
        # Открываем главную страницу
        self.main_page.open()
        
        # Кликаем по кнопке "Личный кабинет"
        self.main_page.click_account_button()
        
        # Проверяем, что перешли в личный кабинет
        self.profile_page.wait_for_profile_page()
        assert self.profile_page.is_profile_visible()

    def test_navigate_from_account_to_constructor_via_button(self):
        """Тест перехода из личного кабинета в конструктор через кнопку 'Конструктор'"""
        # Переходим в личный кабинет
        self.main_page.open()
        self.main_page.click_account_button()
        self.profile_page.wait_for_profile_page()
        
        # Кликаем по кнопке "Конструктор"
        self.main_page.click_constructor_button()
        
        # Проверяем, что перешли на главную страницу
        assert self.main_page.is_constructor_title_visible()

    def test_navigate_from_account_to_constructor_via_logo(self):
        """Тест перехода из личного кабинета в конструктор через логотип"""
        # Переходим в личный кабинет
        self.main_page.open()
        self.main_page.click_account_button()
        self.profile_page.wait_for_profile_page()
        
        # Кликаем по логотипу
        self.main_page.click_logo()
        
        # Проверяем, что перешли на главную страницу
        assert self.main_page.is_constructor_title_visible()

    def test_logout(self):
        """Тест выхода из аккаунта"""
        # Переходим в личный кабинет
        self.main_page.open()
        self.main_page.click_account_button()
        self.profile_page.wait_for_profile_page()
        
        # Выходим из аккаунта
        self.profile_page.click_logout()
        
        # Проверяем, что перешли на страницу логина
        self.login_page.wait_for_url("https://stellarburgers.education-services.ru/login")
        assert self.login_page.is_title_visible()