import unittest
from unittest.mock import patch
from passgen.commands import handle_generate


class TestIntegration(unittest.TestCase):

    def test_generate_password_integration(self):
        args = type('Args', (), {
            'length': 16,
            'uppercase': True,
            'digits': True,
            'special': True
        })()

        password = handle_generate(args)

        self.assertEqual(len(password), 16)
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in "!@#$%^&*" for c in password))

    @patch('passgen.storage.save_password')
    @patch('passgen.storage.find_password')
    def test_save_and_find_integration(self, mock_find, mock_save):
        mock_save.return_value = True
        mock_find.return_value = {
            "service": "test",
            "login": "user",
            "password": "hashed_pass"
        }

        from passgen.commands import handle_save, handle_find

        save_result = handle_save("test", "user", "password123")
        find_result = handle_find("test")

        self.assertTrue(save_result)
        self.assertIsNotNone(find_result)
        self.assertEqual(find_result["service"], "test")


if __name__ == '__main__':
    unittest.main()