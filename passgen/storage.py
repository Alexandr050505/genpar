"""
Модуль работы с хранилищем паролей в PostgreSQL.
"""

import psycopg2
import bcrypt
from datetime import datetime
import os

# Настройки подключения к БД
DB_CONFIG = {
    "dbname": "password_manager",
    "user": "postgres",
    "password": "admin",
    "host": "localhost",
    "port": "5432"
}


def get_connection():
    """Устанавливает соединение с базой данных."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"❌ Ошибка подключения к БД: {e}")
        return None


def init_database():
    """Инициализирует базу данных (создает таблицу если не существует)."""
    conn = get_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_name = 'passwords'
                );
            """)
            exists = cur.fetchone()[0]

            if exists:
                print("✅ База данных готова к работе")
                return True
            else:
                print("❌ Таблица 'passwords' не найдена")
                return False

    except Exception as e:
        print(f"❌ Ошибка инициализации БД: {e}")
        return False
    finally:
        conn.close()


def save_password(service, login, password):
    """
    Сохраняет пароль в базу данных.

    Args:
        service (str): Название сервиса
        login (str): Логин пользователя
        password (str): Пароль для сохранения

    Returns:
        bool: True если успешно, False если ошибка
    """
    conn = get_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cur:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12))

            cur.execute("""
                INSERT INTO passwords (service, login, password_hash) 
                VALUES (%s, %s, %s)
                ON CONFLICT (service) 
                DO UPDATE SET 
                    login = EXCLUDED.login,
                    password_hash = EXCLUDED.password_hash,
                    updated_at = CURRENT_TIMESTAMP
            """, (service, login, hashed_password.decode('utf-8')))

            conn.commit()
            print(f"✅ Пароль для '{service}' сохранен")
            return True

    except Exception as e:
        print(f"❌ Ошибка сохранения пароля: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()


def find_password(service):
    """
    Находит пароль по названию сервиса.

    Args:
        service (str): Название сервиса для поиска

    Returns:
        dict: Словарь с login и password или None если не найден
    """
    conn = get_connection()
    if not conn:
        return None

    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT service, login, password_hash, created_at 
                FROM passwords WHERE service = %s
            """, (service,))

            result = cur.fetchone()

            if result:
                return {
                    "service": result[0],
                    "login": result[1],
                    "password": result[2],
                    "created_at": result[3]
                }
            else:
                return None

    except Exception as e:
        print(f"❌ Ошибка поиска пароля: {e}")
        return None
    finally:
        conn.close()


def get_all_passwords():
    """
    Получает все сохраненные пароли.

    Returns:
        list: Список словарей с информацией о паролях
    """
    conn = get_connection()
    if not conn:
        return []

    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT service, login, created_at 
                FROM passwords ORDER BY service
            """)

            passwords = []
            for row in cur.fetchall():
                passwords.append({
                    "service": row[0],
                    "login": row[1],
                    "created_at": row[2]
                })

            return passwords

    except Exception as e:
        print(f"❌ Ошибка получения списка паролей: {e}")
        return []
    finally:
        conn.close()


def delete_password(service):
    """
    Удаляет пароль по названию сервиса.

    Args:
        service (str): Название сервиса

    Returns:
        bool: True если успешно удалено, False если ошибка
    """
    conn = get_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM passwords WHERE service = %s", (service,))
            conn.commit()

            deleted = cur.rowcount > 0
            if deleted:
                print(f"✅ Пароль для '{service}' удален")
            else:
                print(f"⚠️ Пароль для '{service}' не найден")

            return deleted

    except Exception as e:
        print(f"❌ Ошибка удаления пароля: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()


if __name__ == "__main__":
    print("🧪 Тестирование подключения к БД...")

    # Замените пароль на ваш
    DB_CONFIG["password"] = input("Введите пароль PostgreSQL: ")

    if init_database():
        print("✅ База данных работает!")

        save_password("gmail", "test@gmail.com", "my_password123")

        result = find_password("gmail")
        if result:
            print(f"✅ Найден: {result['service']} - {result['login']}")

        all_passwords = get_all_passwords()
        print(f"📋 Всего паролей: {len(all_passwords)}")

        delete_password("gmail")
    else:
        print("❌ Проблемы с базой данных")