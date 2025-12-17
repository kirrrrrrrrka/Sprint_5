from pages.base_page import BasePage
from locators import RegisterPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/register"
        self.locators = RegisterPageLocators

    def open(self):
        """Открыть страницу регистрации"""
        self.driver.get(self.url)

    def is_title_visible(self):
        """Проверить видимость заголовка 'Регистрация'"""
        return self.is_element_visible(self.locators.TITLE)

    def register(self, name, email, password):
        """Выполнить регистрацию"""
        self.input_text(self.locators.NAME_INPUT, name)
        self.input_text(self.locators.EMAIL_INPUT, email)
        self.input_text(self.locators.PASSWORD_INPUT, password)
        self.click_element(self.locators.REGISTER_BUTTON)

    def click_login_link(self):
        """Кликнуть по ссылке 'Войти'"""
        self.click_element(self.locators.LOGIN_LINK)

    def is_password_error_visible(self):
        """Проверить видимость ошибки 'Некорректный пароль'"""
        return self.is_element_visible(self.locators.PASSWORD_ERROR, timeout=5)

    def get_password_error_text(self):
        """Получить текст ошибки пароля"""
        return self.get_element_text(self.locators.PASSWORD_ERROR)

    def wait_for_registration_result(self, timeout=10):
        """Ожидать результат регистрации - УПРОЩЕННАЯ ВЕРСИЯ"""
        try:
            # Ждем изменения URL или появления ошибки
            WebDriverWait(self.driver, timeout).until(
                lambda d: "login" in d.current_url or 
                         self.is_password_error_visible() or
                         d.current_url != self.url
            )
            return True
        except:
            return False

    def is_registration_successful(self):
        """Проверить успешность регистрации - ПРОСТАЯ ПРОВЕРКА"""
        current_url = self.driver.current_url
        
        # Если перешли на страницу логина - успех
        if "login" in current_url:
            return True
        
        # Если остались на странице регистрации, проверяем не появилась ли ошибка
        if "register" in current_url:
            # Если есть ошибка пароля - регистрация не удалась
            if self.is_password_error_visible():
                return False
            # Иначе считаем успехом (поля должны быть очищены)
            return True
        
        return False