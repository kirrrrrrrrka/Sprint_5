from pages.base_page import BasePage
from locators import ProfilePageLocators


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/account/profile"

    def open(self):
        """Открыть страницу профиля"""
        self.driver.get(self.url)

    def is_profile_visible(self):
        """Проверить видимость раздела 'Профиль'"""
        return self.is_element_visible(ProfilePageLocators.PROFILE_LINK)

    def click_logout(self):
        """Кликнуть по кнопке 'Выход'"""
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    def wait_for_profile_page(self):
        """Ожидать загрузки страницы профиля"""
        self.wait_for_url(self.url)
        return self.is_profile_visible()