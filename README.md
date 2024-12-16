
# Ayame Dox-Bot

## 📖 Описание проекта
Ayame Dox-Bot — это Telegram-бот для анализа телефонных номеров, разрабатывался как маленький аналог "Глаз Бога".

## 🚀 Установка и запуск
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Создайте файл `.env`, используя пример `.env.example`, и добавьте свои токены.
3. Запустите бота:
   ```bash
   python main.py
   ```

## 📋 Команды
- `/start` и `/help` — информация о боте.
- `/account` — проверка статуса учетной записи.
- Отправьте номер телефона для анализа.

## 🛠️ Структура проекта
```
app/
├── bot.py
├── config.py
├── handlers.py
├── api_client.py
├── utils.py
├── cache.py
main.py
.env.example
requirements.txt
README.md
```

## 📚 Дополнительно
Для более подробной инструкции обратитесь к файлу `installation_guide.md`.
