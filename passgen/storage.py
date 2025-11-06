import json
import os

STORAGE_FILE = "passwords.json"


def save_password(service, login, password):
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
    if not os.path.exists(STORAGE_FILE):
        return None

    with open(STORAGE_FILE, 'r') as f:
        data = json.load(f)

    return data.get(service)