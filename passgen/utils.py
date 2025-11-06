"""
Вспомогательные утилиты.

Содержит дополнительные функции для работы с паролями.
"""


def calculate_strength(password):
    """
    Оценивает сложность пароля по шкале от 0 до 4.

    Args:
        password (str): Пароль для оценки

    Returns:
        int: Оценка сложности (0-4)

    Example:
        >>> calculate_strength("StrongPass123!")
        4
    """
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*" for c in password):
        score += 1
    return score