FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Установка playwright и браузеров
RUN playwright install --with-deps chromium

# Установка Allure
RUN apt-get update && \
    apt-get install -y wget default-jre && \
    wget https://github.com/allure-framework/allure2/releases/download/2.21.0/allure-2.21.0.zip && \
    unzip allure-2.21.0.zip -d /opt/ && \
    ln -s /opt/allure-2.21.0/bin/allure /usr/bin/allure && \
    rm allure-2.21.0.zip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Копирование проекта
COPY . .

# Команда по умолчанию для запуска тестов
CMD ["pytest", "-v", "tests/test_main_page.py", "--alluredir=./allure-results"]
