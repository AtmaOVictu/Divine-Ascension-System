import unittest
from divine_agents.binary import text_to_binary

class TestBinaryConversion(unittest.TestCase):
    def test_single_character(self):
        self.assertEqual(text_to_binary('A'), '01000001')

    def test_word(self):
        self.assertEqual(text_to_binary('AB'), '01000001 01000010')

if __name__ == '__main__':
    unittest.main()
