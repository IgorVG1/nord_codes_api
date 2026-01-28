# ИНСТРУКЦИЯ ПО ЗАПУСКУ АВТО-ТЕСТОВ ЧЕРЕЗ ТЕРМИНАЛ (Windows PowerShell)

---

## I. Клонирование репозитория с выполненным заданием
### 1. На рабочем столе создаем новую папку и открываем в ней терминал (Windows PowerShell)
### 2. В терминале выполняем следующие команды по очереди, чтобы перейти в клонированный репозиторий
```bash
git clone https://github.com/IgorVG1/nord_codes_api.git
```
```bash
cd nord_codes_api
```
---

## II. Подготовка к запуску авто-тестов
### 1. Создание виртуального окружения
```bash
python -m venv venv
```
### 2. Активация виртуального окружения
```bash
venv/Scripts/activate
```
### 3. Установка необходимых зависимостей
```bash
pip install -r requirements.txt
```
---

## III. Запуск авто-тестов с генерацией allure-отчета
### 1. Запуск авто-тестов
```bash
pytest -m regression --alluredir=test/allure-results
```
### 2. Просмотр allure-отчета в браузере
```bash
allure serve ./test/allure-results
```
---

## IV. Просмотр исправлений предполагаемых ошибок в архитектуре тестового REST API
### 1. Закрытия allure-отчета
> Press **[Ctrl]** + **[C]** to exit

> Enter **"y"** in console

### 2. Локальный запуск demo-API с исправлениями
```bash
python -m src.main
```
### 3. В браузере открыть страницу по адресу:
> http://127.0.0.1:8000/docs

### 4. После завершения просмотра изменений
> Press **[Ctrl]** + **[C]** to exit

---

## V. Просмотр отчета о найденных ошибках в файле: 
> bug_report.docx

---

## VI. Коллекция в Postman
### 1. Файл формата JSON для прямого импорта:
> nord_codes.postman_collection.json

### 2. Ссылка для просмотра коллекции:
> https://igornevskiy00-5695112.postman.co/workspace/%D0%98%D0%B3%D0%BE%D1%80%D1%8C-%D0%9D%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9's-Workspace~1d5cf416-97d4-466c-843c-d78a82ab5f2b/collection/49077959-861170ef-1fe5-44b8-a305-0bc4d3c64823?action=share&source=copy-link&creator=49077959

---
