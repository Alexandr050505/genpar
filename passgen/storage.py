"""
Модуль работы с хранилищем паролей.

Обеспечивает сохранение и чтение паролей из JSON-файла.
"""

import json
import os

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
        with open(STORAGE_FILE, 'r') as f:
            data = json.load(f)

    data[service] = {
        "login": login,
        "password": password
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

    with open(STORAGE_FILE, 'r') as f:
        data = json.load(f)

    return data.get(service)