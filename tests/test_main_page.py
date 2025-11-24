import pytest
import allure
from pages.main_page import MainPage

@allure.epic("Effective Mobile Website")
@allure.feature("Главная страница - навигация")
class TestMainPageNavigation:
    
    @allure.title("Проверка навигации по разделу '{section_name}'")
    @pytest.mark.parametrize("section_name", [
        "О нас",
        "Контакты",
        "Услуги",
        "Проекты",
        "Карьера",
        "Блог"
    ])
    def test_navigation(self, page, section_name):
        main_page = MainPage(page)
        
        with allure.step("Открытие главной страницы"):
            main_page.open()
        
        with allure.step(f"Переход в раздел '{section_name}'"):
            main_page.navigate_to_section(section_name)
