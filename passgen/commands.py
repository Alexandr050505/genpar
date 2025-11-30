"""
Модуль обработки команд CLI.
"""

from .generator import generate_password
from .storage import save_password, find_password, get_all_passwords, delete_password, init_database

def handle_generate(args):
    """
    Обрабатывает команду генерации пароля.

    Args:
        args: Аргументы командной строки

    Returns:
        str: Сгенерированный пароль
    """
    return generate_password(
        length=args.length,
        use_upper=args.uppercase,
        use_digits=args.digits,
        use_special=args.special
    )

def handle_save(service, login, password):
    """
    Сохраняет пароль в хранилище.

    Args:
        service (str): Название сервиса
        login (str): Логин пользователя
        password (str): Пароль для сохранения
    """
    # Инициализируем базу данных при первом сохранении
    init_database()
    return save_password(service, login, password)

def handle_find(service):
    """
    Находит пароль по названию сервиса.

    Args:
        service (str): Название сервиса для поиска

    Returns:
        dict: Информация о сохраненном пароле или None
    """
    return find_password(service)

def handle_list():
    """
    Показывает все сохраненные пароли.

    Returns:
        list: Список всех сохраненных паролей
    """
    return get_all_passwords()

def handle_delete(service):
    """
    Удаляет пароль по названию сервиса.

    Args:
        service (str): Название сервиса

    Returns:
        bool: True если успешно удалено, False если ошибка
    """
    return delete_password(service)