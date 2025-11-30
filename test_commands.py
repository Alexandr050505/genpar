import unittest
from unittest.mock import patch, MagicMock
from passgen.commands import handle_generate, handle_save, handle_find, handle_list, handle_delete


class TestCommands(unittest.TestCase):

    def setUp(self):
        self.test_args = MagicMock()
        self.test_args.length = 12
        self.test_args.uppercase = True
        self.test_args.digits = True
        self.test_args.special = True

    @patch('passgen.commands.generate_password')
    def test_handle_generate(self, mock_generate):
        mock_generate.return_value = "TestPassword123!"

        result = handle_generate(self.test_args)

        self.assertEqual(result, "TestPassword123!")
        mock_generate.assert_called_once_with(
            length=12,
            use_upper=True,
            use_digits=True,
            use_special=True
        )

    @patch('passgen.commands.save_password')
    @patch('passgen.commands.init_database')
    def test_handle_save(self, mock_init, mock_save):
        mock_save.return_value = True

        result = handle_save("test_service", "test_user", "test_password")

        mock_init.assert_called_once()
        mock_save.assert_called_once_with("test_service", "test_user", "test_password")
        self.assertTrue(result)

    @patch('passgen.commands.find_password')
    def test_handle_find(self, mock_find):
        expected_result = {
            "service": "test_service",
            "login": "test_user",
            "password": "hashed_password"
        }
        mock_find.return_value = expected_result

        result = handle_find("test_service")

        self.assertEqual(result, expected_result)
        mock_find.assert_called_once_with("test_service")

    @patch('passgen.commands.get_all_passwords')
    def test_handle_list(self, mock_get_all):
        expected_result = [
            {"service": "service1", "login": "user1", "created_at": "2025-01-01"},
            {"service": "service2", "login": "user2", "created_at": "2025-01-02"}
        ]
        mock_get_all.return_value = expected_result

        result = handle_list()

        self.assertEqual(result, expected_result)
        mock_get_all.assert_called_once()

    @patch('passgen.commands.delete_password')
    def test_handle_delete(self, mock_delete):
        mock_delete.return_value = True

        result = handle_delete("test_service")

        self.assertTrue(result)
        mock_delete.assert_called_once_with("test_service")


if __name__ == '__main__':
    unittest.main()