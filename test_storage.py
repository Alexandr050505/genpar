import unittest
import os
import tempfile
import json
from unittest.mock import patch, MagicMock
from passgen.storage import save_password, find_password, get_all_passwords, delete_password, init_database


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.test_service = "test_service"
        self.test_login = "test_user"
        self.test_password = "test_password_123"

    @patch('passgen.storage.get_connection')
    def test_save_password_success(self, mock_get_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_connection.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__ = MagicMock(return_value=mock_cursor)
        mock_conn.cursor.return_value.__exit__ = MagicMock(return_value=None)

        result = save_password(self.test_service, self.test_login, self.test_password)

        self.assertTrue(result)
        mock_conn.commit.assert_called_once()

    @patch('passgen.storage.get_connection')
    def test_save_password_failure(self, mock_get_connection):
        mock_get_connection.return_value = None

        result = save_password(self.test_service, self.test_login, self.test_password)

        self.assertFalse(result)

    @patch('passgen.storage.get_connection')
    def test_find_password_exists(self, mock_get_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_connection.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__ = MagicMock(return_value=mock_cursor)
        mock_conn.cursor.return_value.__exit__ = MagicMock(return_value=None)

        mock_cursor.fetchone.return_value = (
            self.test_service,
            self.test_login,
            "hashed_password",
            "2025-01-01 10:00:00"
        )

        result = find_password(self.test_service)

        self.assertIsNotNone(result)
        self.assertEqual(result['service'], self.test_service)
        self.assertEqual(result['login'], self.test_login)

    @patch('passgen.storage.get_connection')
    def test_find_password_not_exists(self, mock_get_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_connection.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__ = MagicMock(return_value=mock_cursor)
        mock_conn.cursor.return_value.__exit__ = MagicMock(return_value=None)

        mock_cursor.fetchone.return_value = None

        result = find_password("non_existent_service")

        self.assertIsNone(result)

    @patch('passgen.storage.get_connection')
    def test_get_all_passwords(self, mock_get_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_connection.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__ = MagicMock(return_value=mock_cursor)
        mock_conn.cursor.return_value.__exit__ = MagicMock(return_value=None)

        mock_cursor.fetchall.return_value = [
            ("service1", "user1", "2025-01-01 10:00:00"),
            ("service2", "user2", "2025-01-01 11:00:00")
        ]

        result = get_all_passwords()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['service'], "service1")
        self.assertEqual(result[1]['login'], "user2")

    @patch('passgen.storage.get_connection')
    def test_delete_password_exists(self, mock_get_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_connection.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__ = MagicMock(return_value=mock_cursor)
        mock_conn.cursor.return_value.__exit__ = MagicMock(return_value=None)

        mock_cursor.rowcount = 1

        result = delete_password(self.test_service)

        self.assertTrue(result)
        mock_conn.commit.assert_called_once()

    @patch('passgen.storage.get_connection')
    def test_delete_password_not_exists(self, mock_get_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_connection.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__ = MagicMock(return_value=mock_cursor)
        mock_conn.cursor.return_value.__exit__ = MagicMock(return_value=None)

        mock_cursor.rowcount = 0

        result = delete_password("non_existent_service")

        self.assertFalse(result)

    @patch('passgen.storage.get_connection')
    def test_init_database_success(self, mock_get_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_connection.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__ = MagicMock(return_value=mock_cursor)
        mock_conn.cursor.return_value.__exit__ = MagicMock(return_value=None)

        mock_cursor.fetchone.return_value = [True]

        result = init_database()

        self.assertTrue(result)

    @patch('passgen.storage.get_connection')
    def test_init_database_failure(self, mock_get_connection):
        mock_get_connection.return_value = None

        result = init_database()

        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()