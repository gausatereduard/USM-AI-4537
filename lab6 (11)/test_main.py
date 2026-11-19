import unittest

from main import recognize


class RecognizerTests(unittest.TestCase):
    def test_accepts_nonempty_even_lengths(self):
        for text in ("aa", "aaaa", "aaaaaa", "a" * 10_000):
            with self.subTest(length=len(text)):
                self.assertTrue(recognize(text))

    def test_rejects_empty(self):
        self.assertFalse(recognize(""))

    def test_rejects_odd_lengths(self):
        for text in ("a", "aaa", "aaaaa"):
            with self.subTest(text=text):
                self.assertFalse(recognize(text))

    def test_rejects_other_characters(self):
        for text in ("ab", "aabbaa", "AA", "aa a", "aa\n\n", "a\u0430"):
            with self.subTest(text=text):
                self.assertFalse(recognize(text))
