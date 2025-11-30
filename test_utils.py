import unittest
from passgen.utils import calculate_strength

class TestPasswordStrength(unittest.TestCase):
    def test_weak_password(self):
        score = calculate_strength("abc")
        self.assertEqual(score, 0)

    def test_medium_password_length_only(self):
        score = calculate_strength("abcdefgh")
        self.assertEqual(score, 1)

    def test_medium_password_with_upper(self):
        score = calculate_strength("Abcdefgh")
        self.assertEqual(score, 2)

    def test_strong_password_with_upper_digits(self):
        score = calculate_strength("Abcdefgh123")
        self.assertEqual(score, 3)

    def test_very_strong_password(self):
        score = calculate_strength("StrongPass123!")
        self.assertEqual(score, 4)

    def test_password_with_special_only(self):
        score = calculate_strength("!!!!!!!!")  # Изменил на 8 символов
        self.assertEqual(score, 2)

    def test_empty_password(self):
        score = calculate_strength("")
        self.assertEqual(score, 0)

    def test_none_password(self):
        with self.assertRaises(TypeError):
            calculate_strength(None)