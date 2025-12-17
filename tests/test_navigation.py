import pytest


class TestNavigation:
    def test_navigate_to_account_from_main(self, driver, main_page, profile_page, logged_in_user):
        """Тест перехода в личный кабинет с главной страницы"""
        # Открываем главную страницу
        main_page.open()
        
        # Кликаем по кнопке "Личный кабинет"
        main_page.click_account_button()
        
        # Проверяем, что перешли в личный кабинет
        assert profile_page.wait_for_profile_page(), "Не удалось перейти в личный кабинет"
        assert profile_page.is_profile_visible(), "Раздел 'Профиль' не виден"

    def test_navigate_from_account_to_constructor_via_button(self, driver, main_page, profile_page, logged_in_user):
        """Тест перехода из личного кабинета в конструктор через кнопку 'Конструктор'"""
        # Переходим в личный кабинет
        main_page.open()
        main_page.click_account_button()
        assert profile_page.wait_for_profile_page(), "Не удалось перейти в личный кабинет"
        
        # Кликаем по кнопку "Конструктор"
        main_page.click_constructor_button()
        
        # Проверяем, что перешли на главную страницу
        assert main_page.is_constructor_title_visible(), "Не удалось перейти в конструктор через кнопку"

    def test_navigate_from_account_to_constructor_via_logo(self, driver, main_page, profile_page, logged_in_user):
        """Тест перехода из личного кабинета в конструктор через логотип"""
        # Переходим в личный кабинет
        main_page.open()
        main_page.click_account_button()
        assert profile_page.wait_for_profile_page(), "Не удалось перейти в личный кабинет"
        
        # Кликаем по логотипу
        main_page.click_logo()
        
        # Проверяем, что перешли на главную страницу
        assert main_page.is_constructor_title_visible(), "Не удалось перейти в конструктор через логотип"

    def test_logout(self, driver, main_page, login_page, profile_page, logged_in_user):
        """Тест выхода из аккаунта"""
        # Переходим в личный кабинет
        main_page.open()
        main_page.click_account_button()
        assert profile_page.wait_for_profile_page(), "Не удалось перейти в личный кабинет"
        
        # Выходим из аккаунта
        profile_page.click_logout()
        
        # Проверяем, что перешли на страницу логина
        assert login_page.wait_for_url("https://stellarburgers.education-services.ru/login"), "Не удалось выйти из аккаунта"
        assert login_page.is_title_visible(), "Страница логина не загрузилась"