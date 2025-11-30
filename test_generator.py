import unittest
import string
from passgen.generator import generate_password


class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        password = generate_password()
        self.assertEqual(len(password), 12)

    def test_custom_length(self):
        password = generate_password(length=15)
        self.assertEqual(len(password), 15)

    def test_uppercase_chars(self):
        password = generate_password(use_upper=True)
        has_upper = any(c.isupper() for c in password)
        self.assertTrue(has_upper)

    def test_no_uppercase_chars(self):
        password = generate_password(use_upper=False)
        has_upper = any(c.isupper() for c in password)
        self.assertFalse(has_upper)

    def test_digits_chars(self):
        password = generate_password(use_digits=True)
        has_digits = any(c.isdigit() for c in password)
        self.assertTrue(has_digits)

    def test_no_digits_chars(self):
        password = generate_password(use_digits=False)
        has_digits = any(c.isdigit() for c in password)
        self.assertFalse(has_digits)

    def test_special_chars(self):
        password = generate_password(use_special=True)
        has_special = any(c in "!@#$%^&*" for c in password)
        self.assertTrue(has_special)

    def test_no_special_chars(self):
        password = generate_password(use_special=False)
        has_special = any(c in "!@#$%^&*" for c in password)
        self.assertFalse(has_special)

    def test_all_features(self):
        password = generate_password(
            length=20,
            use_upper=True,
            use_digits=True,
            use_special=True
        )
        self.assertEqual(len(password), 20)
        has_upper = any(c.isupper() for c in password)
        has_digits = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*" for c in password)
        self.assertTrue(has_upper)
        self.assertTrue(has_digits)
        self.assertTrue(has_special)

    def test_only_lowercase(self):
        password = generate_password(
            use_upper=False,
            use_digits=False,
            use_special=False
        )
        self.assertTrue(all(c in string.ascii_lowercase for c in password))


if __name__ == '__main__':
    unittest.main()