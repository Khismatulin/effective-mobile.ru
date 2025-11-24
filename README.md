# Тестирование навигации на сайте Effective Mobile

Этот проект содержит автоматизированные UI-тесты для проверки навигации на главной странице сайта effective-mobile.ru.

## Технологии и инструменты

- Python 3.10
- Playwright
- Pytest
- Allure Reports
- Docker

## Структура проекта

project/
- Dockerfile               # Настройки Docker-контейнера
- docker-compose.yml       # Оркестрация контейнеров
- requirements.txt         # Зависимости Python
- README.md                # Документация проекта
- conftest.py              # Конфигурация и фикстуры Pytest
- pages/                   # Директория с Page Objects
  - __init__.py          # Делает директорию Python-пакетом
  - base_page.py         # Базовый класс для всех страниц
  - main_page.py         # Page Object главной страницы
- tests/                   # Директория с тестами
  - __init__.py          # Делает директорию Python-пакетом
  - test_main_page.py    # Тесты навигации
- .gitignore               # Файлы, исключаемые из Git

## Запуск тестов

  ### Локальный запуск
  
  1. Установите Python 3.10
  2. Установите зависимости:
      ```bash
      pip install -r requirements.txt
  3. Установите Playwright и браузеры:
     
    playwright install --with-deps chromium
  5. Запустите тесты:
     
    pytest tests/test_main_page.py --alluredir=./allure-results
  7. Сгенерируйте отчет Allure:
     
    allure serve ./allure-results

### Запуск в Docker

1. Убедитесь, что у вас установлены Docker и Docker Compose
2. Запустите тесты и сервис Allure с помощью Docker Compose:
   ```bash
    docker-compose up
4. Откройте отчет Allure в браузере по адресу: http://localhost:5050
