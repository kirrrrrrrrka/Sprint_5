from pages.base_page import BasePage
from locators import MainPageLocators, ConstructorPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/"

    def open(self):
        """Открыть главную страницу"""
        self.driver.get(self.url)

    def click_login_button(self):
        """Кликнуть по кнопке 'Войти в аккаунт'"""
        self.click_element(MainPageLocators.LOGIN_BUTTON)

    def click_account_button(self):
        """Кликнуть по кнопке 'Личный Кабинет'"""
        self.click_element(MainPageLocators.ACCOUNT_BUTTON)

    def click_constructor_button(self):
        """Кликнуть по кнопке 'Конструктор'"""
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_logo(self):
        """Кликнуть по логотипу"""
        self.click_element(MainPageLocators.LOGO)

    def is_constructor_title_visible(self):
        """Проверить видимость заголовка конструктора"""
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_TITLE)

    def click_buns_section(self):
        """Кликнуть по разделу 'Булки'"""
        self.click_element(ConstructorPageLocators.BUNS_SECTION)

    def click_sauces_section(self):
        """Кликнуть по разделу 'Соусы'"""
        self.click_element(ConstructorPageLocators.SAUCES_SECTION)

    def click_fillings_section(self):
        """Кликнуть по разделу 'Начинки'"""
        self.click_element(ConstructorPageLocators.FILLINGS_SECTION)

    def is_buns_selected(self):
        """Проверить, что выбран раздел 'Булки'"""
        return self.is_element_visible(ConstructorPageLocators.BUNS_SELECTED)

    def is_sauces_selected(self):
        """Проверить, что выбран раздел 'Соусы'"""
        return self.is_element_visible(ConstructorPageLocators.SAUCES_SELECTED)

    def is_fillings_selected(self):
        """Проверить, что выбран раздел 'Начинки'"""
        return self.is_element_visible(ConstructorPageLocators.FILLINGS_SELECTED)