import pytest
import allure
from playwright.sync_api import sync_playwright
from pytest import fixture

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Настройка контекста браузера"""
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
    }

@fixture(scope="function")
def page(browser):
    """Фикстура для создания страницы"""
    context = browser.new_context()
    page = context.new_page()
    
    # Действия перед тестом
    yield page
    
    # Действия после теста
    if pytest.result_storage:
        test_name = f"{request.node.name}"
        if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
            screenshot = page.screenshot(path=None, full_page=True)
            allure.attach(
                screenshot,
                name="screenshot_failure",
                attachment_type=allure.attachment_type.PNG
            )
    
    # Закрываем контекст после теста
    context.close()
