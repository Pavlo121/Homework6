class StringProcessor:
    """
    Клас для обробки рядків, що включає методи для перевертання рядка,
    капіталізації першої літери та підрахунку голосних.
    """

    def reverse_string(self, s: str) -> str:
        """Перевертає рядок у зворотному порядку."""
        return s[::-1]

    def capitalize_string(self, s: str) -> str:
        """Капіталізує перший символ рядка, якщо це можливо."""
        return s.capitalize()

    def count_vowels(self, s: str) -> int:
        """Підраховує кількість голосних у рядку."""
        vowels = "aeiouAEIOU"
        return sum(1 for char in s if char in vowels)


import unittest


class TestStringProcessor(unittest.TestCase):
    """Тестування методів класу StringProcessor."""

    def setUp(self):
        """Ініціалізує об'єкт StringProcessor перед кожним тестом."""
        self.processor = StringProcessor()

    # Тестування reverse_string з кількома сценаріями
    def test_reverse_string(self):
        """Тестує метод reverse_string з різними вхідними даними."""
        self.assertEqual(self.processor.reverse_string(""), "")
        self.assertEqual(self.processor.reverse_string("Hello"), "olleH")
        self.assertEqual(self.processor.reverse_string("hElLo"), "oLlEh")
        self.assertEqual(self.processor.reverse_string("123abc!@#"), "#@!cba321")
        self.assertEqual(self.processor.reverse_string(""), "")

    # Пропуск тесту для порожнього рядка
    @unittest.skip("Пропускається, відома проблема з порожніми рядками")
    def test_reverse_string_empty(self):
        """Тестує метод reverse_string з порожнім рядком."""
        self.assertEqual(self.processor.reverse_string(""), "")

    # Тестування capitalize_string з кількома сценаріями
    def test_capitalize_string(self):
        """Тестує метод capitalize_string з різними вхідними даними."""
        self.assertEqual(self.processor.capitalize_string(""), "")
        self.assertEqual(self.processor.capitalize_string("hello"), "Hello")
        self.assertEqual(self.processor.capitalize_string("HELLO"), "Hello")
        self.assertEqual(self.processor.capitalize_string("hElLo"), "Hello")
        self.assertEqual(self.processor.capitalize_string("123abc"), "123abc")
        self.assertEqual(self.processor.capitalize_string("!hello"), "!hello")

    # Тестування count_vowels з кількома сценаріями
    def test_count_vowels(self):
        """Тестує метод count_vowels на підрахунок голосних у різних рядках."""
        self.assertEqual(self.processor.count_vowels(""), 0)
        self.assertEqual(self.processor.count_vowels("hello"), 2)
        self.assertEqual(self.processor.count_vowels("HELLO"), 2)
        self.assertEqual(self.processor.count_vowels("hElLo"), 2)
        self.assertEqual(self.processor.count_vowels("123abc!@#"), 1)
        self.assertEqual(self.processor.count_vowels("bcdfgh"), 0)
        self.assertEqual(self.processor.count_vowels("aeiouAEIOU"), 10)


if __name__ == '__main__':
    unittest.main()
