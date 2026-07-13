# Sprint 6 — Яндекс.Самокат

Автотесты для учебного сервиса [Яндекс.Самокат](https://qa-scooter.praktikum-services.ru/).

## Стек

- Python 3
- Selenium WebDriver
- pytest
- Allure
- Firefox

## Установка

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Запуск тестов

```bash
pytest
```

## Allure-отчёт

```bash
allure serve allure_results
```

Или сгенерировать статический отчёт:

```bash
allure generate allure_results -o allure-report --clean
```
