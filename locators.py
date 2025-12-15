from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы"""
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")


class LoginPageLocators:
    """Локаторы для страницы авторизации"""
    TITLE = (By.XPATH, ".//h2[text()='Вход']")
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")


class RegisterPageLocators:
    """Локаторы для страницы регистрации"""
    TITLE = (By.XPATH, ".//h2[text()='Регистрация']")
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.LINK_TEXT, "Войти")
    PASSWORD_ERROR = (By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]")


class ForgotPasswordPageLocators:
    """Локаторы для страницы восстановления пароля"""
    TITLE = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    LOGIN_LINK = (By.LINK_TEXT, "Войти")


class ProfilePageLocators:
    """Локаторы для страницы профиля в личном кабинете"""
    PROFILE_LINK = (By.XPATH, ".//a[text()='Профиль']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")


class ConstructorPageLocators:
    """Локаторы для конструктора бургеров на главной странице"""
    BUNS_SECTION = (By.XPATH, ".//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, ".//span[text()='Начинки']/parent::div")
    BUNS_SELECTED = (By.XPATH, ".//div[contains(@class, 'current')]//span[text()='Булки']")
    SAUCES_SELECTED = (By.XPATH, ".//div[contains(@class, 'current')]//span[text()='Соусы']")
    FILLINGS_SELECTED = (By.XPATH, ".//div[contains(@class, 'current')]//span[text()='Начинки']")