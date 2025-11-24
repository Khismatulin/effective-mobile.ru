import allure
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page, url: str = ""):
        self.page = page
        self.url = url
    
    @allure.step("Открытие страницы {self.url}")
    def open(self):
        self.page.goto(self.url)
        return self
    
    @allure.step("Клик по элементу {selector}")
    def click(self, selector: str):
        self.page.click(selector)
        return self
    
    @allure.step("Проверка наличия элемента {selector}")
    def should_have_element(self, selector: str):
        expect(self.page.locator(selector)).to_be_visible()
        return self
    
    @allure.step("Проверка URL содержит {url_part}")
    def should_have_url_containing(self, url_part: str):
        expect(self.page).to_have_url(url_part, timeout=5000)
        return self
    
    @allure.step("Ожидание загрузки страницы")
    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")
        return self
    
    @allure.step("Создание скриншота")
    def take_screenshot(self, name="screenshot"):
        screenshot = self.page.screenshot()
        allure.attach(
            screenshot,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
        return self
