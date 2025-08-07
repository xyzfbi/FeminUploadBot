# FeminUploadBot

**FeminUploadBot** — это Telegram-бот, предназначенный для загрузки музыкальных треков на платформу [Femin](https://github.com/lyweze/femin). Он упрощает процесс отправки треков (включая треки из Яндекс Музыки) напрямую в сервис обмена музыкой Femin, позволяя пользователям легко делиться и управлять загрузками.

## Возможности

- **Загрузка треков на Femin:** Отправляйте музыкальные треки напрямую на платформу Femin через Telegram.
- **Интеграция с Яндекс Музыкой:** Загружайте треки по ссылкам из Яндекс Музыки.
- **Простые команды:**
  - `/start` — Приветствие и главное меню
  - `/help` — Помощь и инструкция по использованию
  - `/yandex` — Загрузка трека из Яндекс Музыки
- **Удобные клавиатуры:** Быстрый доступ к основным действиям через клавиатуру Telegram.

## Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/yourusername/FeminUploadBot.git
   cd FeminUploadBot
   ```

2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Настройте переменные окружения:**
   - Скопируйте `env_example.txt` в `.env` и заполните своими значениями для Supabase, Яндекс Музыки и Telegram Bot.

4. **Запустите бота:**
   ```bash
   python main.py
   ```
   Или используйте скрипт `start.sh`.

## Переменные окружения

Вам необходимо указать следующие переменные в файле `.env`:
```
SUPABASE_URL=your_supabase_project_url_here
SUPABASE_ANON_KEY=your_supabase_anon_key_here
SUPABASE_SERVICE_KEY=your_supabase_service_role_key_here
YANDEX_TOKEN=your_yandex_music_token_here
DEFAULT_COVER=your_default_cover_url_here
TELEGRAM_TOKEN=your_telegram_bot_token_here
```

## Структура проекта

- `main.py` — Точка входа для бота
- `handlers/` — Обработчики команд и сообщений Telegram
- `keyboards/` — Описания клавиатур
- `services/yandex_music/` — Логика интеграции с Яндекс Музыкой
- `database/` — Подключение к Supabase и работа с БД
- `config/` — Управление переменными окружения

## Вклад

Pull requests и предложения приветствуются!

---

**Кратко:**  
Это Telegram-бот для загрузки музыки на платформу Femin с поддержкой Яндекс Музыки и Supabase. Легко настраивается и используется, предназначен для музыкальных сообществ.
