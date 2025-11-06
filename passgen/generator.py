import random
import string


def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    chars = string.ascii_lowercase

    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*"

    return ''.join(random.choice(chars) for _ in range(length))