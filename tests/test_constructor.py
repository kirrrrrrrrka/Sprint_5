import pytest


class TestConstructor:
    def test_navigate_to_buns_section(self, driver, main_page):
        """Тест перехода к разделу 'Булки'"""
        # Открываем главную страницу
        main_page.open()
        
        # Переходим к другому разделу, чтобы потом вернуться к булкам
        main_page.click_sauces_section()
        assert main_page.is_sauces_selected(), "Раздел 'Соусы' не выбран"
        
        # Переходим к разделу "Булки"
        main_page.click_buns_section()
        
        # Проверяем, что раздел "Булки" выбран
        assert main_page.is_buns_selected(), "Раздел 'Булки' не выбран"

    def test_navigate_to_sauces_section(self, driver, main_page):
        """Тест перехода к разделу 'Соусы'"""
        # Открываем главную страницу
        main_page.open()
        
        # Переходим к разделу "Соусы"
        main_page.click_sauces_section()
        
        # Проверяем, что раздел "Соусы" выбран
        assert main_page.is_sauces_selected(), "Раздел 'Соусы' не выбран"

    def test_navigate_to_fillings_section(self, driver, main_page):
        """Тест перехода к разделу 'Начинки'"""
        # Открываем главную страницу
        main_page.open()
        
        # Переходим к разделу "Начинки"
        main_page.click_fillings_section()
        
        # Проверяем, что раздел "Начинки" выбран
        assert main_page.is_fillings_selected(), "Раздел 'Начинки' не выбран"