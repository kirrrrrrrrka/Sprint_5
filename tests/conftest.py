import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.profile_page import ProfilePage
from pages.forgotpass_page import ForgotPasswordPage
from generators import generate_email, generate_name, generate_password


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to run tests: chrome or firefox")
    parser.addoption("--headless", action="store_true", default=False, help="run in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    
    driver = None
    
    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")
    
    driver.implicitly_wait(5)
    
    yield driver
    
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def register_page(driver):
    return RegisterPage(driver)


@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver)


@pytest.fixture
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)


@pytest.fixture
def registered_user(driver, register_page, login_page):
    """Фикстура для регистрации пользователя и получения его данных"""
    name = generate_name()
    email = generate_email()
    password = generate_password(8)  # Используем твою функцию с min_length=8
    
    register_page.open()
    register_page.register(name, email, password)
    
    # Ждем результата регистрации
    assert register_page.wait_for_registration_result(), "Не дождались результата регистрации"
    
    # Проверяем успешность регистрации
    if register_page.is_password_error_visible():
        # Если есть ошибка пароля, регистрируем с нормальным паролем
        password = generate_password(8)  # Генерируем нормальный пароль
        register_page.open()
        register_page.register(name, email, password)
        assert register_page.wait_for_registration_result(), "Повторная регистрация не удалась"
    
    return {
        "name": name,
        "email": email,
        "password": password
    }


@pytest.fixture
def logged_in_user(driver, main_page, login_page, register_page):
    """Фикстура для регистрации и логина пользователя"""
    name = generate_name()
    email = generate_email()
    password = generate_password(8)
    
    # Регистрируем пользователя
    register_page.open()
    register_page.register(name, email, password)
    
    # Ждем результата регистрации
    assert register_page.wait_for_registration_result(), "Не дождались результата регистрации"
    
    # Если есть ошибка пароля, пробуем еще раз
    if register_page.is_password_error_visible():
        password = generate_password(8)
        register_page.open()
        register_page.register(name, email, password)
        assert register_page.wait_for_registration_result(), "Повторная регистрация не удалась"
    
    # Логинимся
    login_page.login(email, password)
    
    # Проверяем, что залогинились
    assert main_page.is_constructor_title_visible(), "Не удалось войти в систему"
    
    return {
        "name": name,
        "email": email,
        "password": password
    }