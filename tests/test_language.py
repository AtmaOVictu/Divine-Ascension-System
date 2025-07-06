import unittest
from divine_agents.language import English, Slovene


class TestLanguage(unittest.TestCase):
    def test_translation(self):
        eng = English()
        slo = Slovene()
        self.assertEqual(eng.translate("hello"), "Hello")
        self.assertEqual(slo.translate("hello"), "Pozdravljeni")
        self.assertEqual(eng.translate("missing"), "missing")


if __name__ == '__main__':
    unittest.main()
