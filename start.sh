#!/bin/bash

# Создание виртуальной среды
python -m venv venv

# Активация виртуальной среды
source venv/bin/activate

# Установка зависимостей из requirements.txt
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "Файл requirements.txt не найден."
fi
