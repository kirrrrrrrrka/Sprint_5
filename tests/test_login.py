import pytest


class TestLogin:
    def test_login_from_main_page_login_button(self, driver, main_page, login_page, registered_user):
        """Тест входа через кнопку 'Войти в аккаунт' на главной"""
        # Открываем главную страницу
        main_page.open()
        
        # Кликаем по кнопке "Войти в аккаунт"
        main_page.click_login_button()
        
        # Выполняем вход
        login_page.login(registered_user["email"], registered_user["password"])
        
        # Проверяем, что перешли на главную страницу
        assert main_page.is_constructor_title_visible(), "Не удалось войти через кнопку 'Войти в аккаунт'"

    def test_login_from_account_button(self, driver, main_page, login_page, registered_user):
        """Тест входа через кнопку 'Личный кабинет'"""
        # Открываем главную страницу
        main_page.open()
        
        # Кликаем по кнопке "Личный кабинет" (без авторизации)
        main_page.click_account_button()
        
        # Выполняем вход
        login_page.login(registered_user["email"], registered_user["password"])
        
        # Проверяем, что перешли на главную страницу
        assert main_page.is_constructor_title_visible(), "Не удалось войти через кнопку 'Личный кабинет'"

    def test_login_from_register_page(self, driver, register_page, login_page, main_page, registered_user):
        """Тест входа через кнопку в форме регистрации"""
        # Открываем страницу регистрации
        register_page.open()
        
        # Кликаем по ссылке "Войти" на странице регистрации
        register_page.click_login_link()
        
        # Выполняем вход
        login_page.login(registered_user["email"], registered_user["password"])
        
        # Проверяем, что перешли на главную страницу
        assert main_page.is_constructor_title_visible(), "Не удалось войти через форму регистрации"

    def test_login_from_forgot_password_page(self, driver, forgot_password_page, login_page, main_page, registered_user):
        """Тест входа через кнопку в форме восстановления пароля"""
        # Открываем страницу восстановления пароля
        forgot_password_page.open()
        
        # Кликаем по ссылке "Войти" на странице восстановления пароля
        forgot_password_page.click_login_link()
        
        # Выполняем вход
        login_page.login(registered_user["email"], registered_user["password"])
        
        # Проверяем, что перешли на главную страницу
        assert main_page.is_constructor_title_visible(), "Не удалось войти через форму восстановления пароля"