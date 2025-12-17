import pytest
from generators import generate_email, generate_name, generate_password


class TestRegistration:
    def test_successful_registration(self, driver, register_page, login_page):
        """Тест успешной регистрации"""
        name = generate_name()
        email = generate_email()
        password = generate_password(8)  # Используем твою функцию с min_length=8
        
        register_page.open()
        assert register_page.is_title_visible(), "Страница регистрации не загрузилась"
        
        register_page.register(name, email, password)
        
        # Ждем результата
        assert register_page.wait_for_registration_result(), "Не дождались результата регистрации"
        
        # Проверяем, что нет ошибки пароля
        assert not register_page.is_password_error_visible(), \
            f"Появилась ошибка пароля при регистрации с паролем длиной {len(password)} символов"

    def test_registration_with_invalid_password(self, driver, register_page):
        """Тест регистрации с некорректным паролем (менее 6 символов)"""
        name = generate_name()
        email = generate_email()
        password = "12345"  # 5 символов - НЕКОРРЕКТНО!
        
        register_page.open()
        assert register_page.is_title_visible(), "Страница регистрации не загрузилась"
        
        # Заполняем форму с коротким паролем
        register_page.register(name, email, password)
        
        # Ждем появления ошибки
        assert register_page.wait_for_registration_result(), "Не дождались результата регистрации"
        
        # Проверяем, что ошибка появилась
        assert register_page.is_password_error_visible(), \
            "После нажатия кнопки 'Зарегистрироваться' с коротким паролем должна появиться ошибка 'Некорректный пароль'"
        
        # Проверяем текст ошибки
        error_text = register_page.get_password_error_text()
        assert error_text and "Некорректный пароль" in error_text, \
            f"Текст ошибки должен содержать 'Некорректный пароль', получено: '{error_text}'"
        
        # Проверяем, что остались на странице регистрации
        current_url = driver.current_url
        assert "register" in current_url, \
            f"При некорректном пароле должны остаться на странице регистрации, а перешли на: {current_url}"