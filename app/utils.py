
def format_response(data):
    """Форматирует ответ API в удобный текст."""
    callapp = data.get('callapp', {})
    return f"""
📞 Номер: {callapp.get('number')}
🧑 Имя: {callapp.get('name', 'Неизвестно')}
⭐ Рейтинг: {callapp.get('avgRating', 'N/A')}
⚠️ Спам-оценка: {callapp.get('spamScore', 'N/A')}
    """
