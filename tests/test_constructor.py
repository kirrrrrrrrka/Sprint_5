import pytest
from pages.main_page import MainPage


class TestConstructor:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)

    def test_navigate_to_buns_section(self):
        """Тест перехода к разделу 'Булки'"""
        # Открываем главную страницу
        self.main_page.open()
        
        # Переходим к другому разделу, чтобы потом вернуться к булкам
        self.main_page.click_sauces_section()
        assert self.main_page.is_sauces_selected()
        
        # Переходим к разделу "Булки"
        self.main_page.click_buns_section()
        
        # Проверяем, что раздел "Булки" выбран
        assert self.main_page.is_buns_selected()

    def test_navigate_to_sauces_section(self):
        """Тест перехода к разделу 'Соусы'"""
        # Открываем главную страницу
        self.main_page.open()
        
        # Переходим к разделу "Соусы"
        self.main_page.click_sauces_section()
        
        # Проверяем, что раздел "Соусы" выбран
        assert self.main_page.is_sauces_selected()

    def test_navigate_to_fillings_section(self):
        """Тест перехода к разделу 'Начинки'"""
        # Открываем главную страницу
        self.main_page.open()
        
        # Переходим к разделу "Начинки"
        self.main_page.click_fillings_section()
        
        # Проверяем, что раздел "Начинки" выбран
        assert self.main_page.is_fillings_selected()
    