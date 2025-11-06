"""
Модуль генерации паролей.

Содержит функции для создания случайных безопасных паролей.
"""

import random
import string


def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    """
    Генерирует случайный пароль с заданными параметрами.

    Args:
        length (int): Длина пароля (по умолчанию 12)
        use_upper (bool): Использовать заглавные буквы
        use_digits (bool): Использовать цифры
        use_special (bool): Использовать специальные символы

    Returns:
        str: Сгенерированный пароль

    Example:
        >>> generate_password(length=8)
        'k8f#m2pL'
    """
    chars = string.ascii_lowercase

    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*"

    return ''.join(random.choice(chars) for _ in range(length))