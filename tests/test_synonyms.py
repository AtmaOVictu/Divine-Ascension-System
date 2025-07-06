import unittest
from divine_agents.synonyms import OntoSynonymAnalyzer


class TestSynonymAnalyzer(unittest.TestCase):
    def test_correct_synonym(self):
        analyzer = OntoSynonymAnalyzer()
        self.assertFalse(analyzer.check_synonym_error("omogočiti", "aktivirati"))

    def test_incorrect_synonym(self):
        analyzer = OntoSynonymAnalyzer()
        self.assertTrue(analyzer.check_synonym_error("omogočiti", "dovoliti"))
        message = analyzer.explain("omogočiti", "dovoliti")
        self.assertIn("nista pravilna sinonima", message)


if __name__ == "__main__":
    unittest.main()
