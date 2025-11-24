import allure
from .base_page import BasePage

class MainPage(BasePage):
    # URL главной страницы
    URL = "https://effective-mobile.ru/"
    
    # Селекторы для основных блоков навигации
    ABOUT_US_LINK = "a[href*='#about']"
    VACANCIES_LINK = "a[href*='#specializations']"
    REVIEWS_LINK = "a[href*='#testimonials']"
    CONTACTS_LINK = "a[href*='#contact']"
    
    # Карта селекторов и ожидаемых URL для параметризованного тестирования
    NAVIGATION_MAP = {
        "О нас": {"selector": ABOUT_US_LINK, "url_part": "/#about"},
        "Контакты": {"selector": VACANCIES_LINK, "url_part": "/#specializations"},
        "Услуги": {"selector": REVIEWS_LINK, "url_part": "/#testimonials"},
        "Проекты": {"selector": CONTACTS_LINK, "url_part": "/#contact"}
    }
    
    def __init__(self, page):
        super().__init__(page, self.URL)
    
    @allure.step("Переход в раздел '{section_name}'")
    def navigate_to_section(self, section_name):
        if section_name in self.NAVIGATION_MAP:
            section = self.NAVIGATION_MAP[section_name]
            self.click(section["selector"])
            self.wait_for_page_load()
            self.should_have_url_containing(section["url_part"])
            self.take_screenshot(f"{section_name}_page")
        else:
            raise ValueError(f"Неизвестный раздел: {section_name}")
        return self
