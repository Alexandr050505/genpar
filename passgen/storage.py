"""
Модуль работы с хранилищем паролей.

Обеспечивает сохранение и чтение паролей из JSON-файла.
"""

import json
import os
import bcrypt

STORAGE_FILE = "passwords.json"


def save_password(service, login, password):
    """
    Сохраняет пароль в JSON-файл.

    Args:
        service (str): Название сервиса
        login (str): Логин пользователя
        password (str): Пароль для сохранения

    Raises:
        IOError: Если произошла ошибка записи в файл
    """
    data = {}

    if os.path.exists(STORAGE_FILE):
        try:
            with open(STORAGE_FILE, 'r') as f:
                content = f.read().strip()
                if content:  # Проверяем, что файл не пустой
                    data = json.loads(content)
        except (json.JSONDecodeError, ValueError):
            # Если файл поврежден, создаем новый
            print(f"Warning: Storage file corrupted. Creating new one.")
            data = {}

    # Конвертируем bytes в строку для сериализации JSON
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12))

    data[service] = {
        "login": login,
        "password": hashed_password.decode('utf-8')  # Конвертируем bytes в строку
    }

    with open(STORAGE_FILE, 'w') as f:
        json.dump(data, f, indent=2)
def find_password(service):
    """
    Находит пароль по названию сервиса.

    Args:
        service (str): Название сервиса для поиска

    Returns:
        dict: Словарь с login и password или None если не найден

    Raises:
        FileNotFoundError: Если файл хранилища не существует
    """
    if not os.path.exists(STORAGE_FILE):
        return None

    try:
        with open(STORAGE_FILE, 'r') as f:
            content = f.read().strip()
            if not content:
                return None
            data = json.loads(content)
    except (json.JSONDecodeError, ValueError):
        print(f"Error: Storage file is corrupted.")
        return None

    return data.get(service)