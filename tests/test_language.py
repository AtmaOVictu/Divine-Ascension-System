import unittest

from divine_agents.language import English, Slovenian


class TestLanguage(unittest.TestCase):
    def test_english_greet(self):
        self.assertEqual(English().greet(), "Hello")
        self.assertEqual(English().farewell(), "Goodbye")

    def test_slovenian_greet(self):
        self.assertEqual(Slovenian().greet(), "Pozdravljeni")
        self.assertEqual(Slovenian().farewell(), "Nasvidenje")


if __name__ == "__main__":
    unittest.main()
