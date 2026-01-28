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
```bash
cd nord_codes_api
```

## II. Подготовка к запуску авто-тестов
### 1. Создание виртуального окружения
```bash
python -m venv venv
```
### 2. Активация виртуального окружения
```bash
venv/Scripts/activate
```
### Установка необходимых зависимостей
```bash
pip install -r requirements.txt
```