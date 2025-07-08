import unittest
from divine_agents.dictionary import OntologicalDictionary
from divine_agents.writer import WritingAgent, ReflectiveWritingAgent


class TestDictionaryWriter(unittest.TestCase):
    def test_dictionary_lookup(self):
        od = OntologicalDictionary()
        meaning = od.get_word_meaning("calm")
        self.assertEqual(meaning["emotion"], "positive")

    def test_writing_agent(self):
        writer = WritingAgent("scribe")
        writer.write_event("test", "joy", "thinking")
        self.assertEqual(len(writer.review_history()), 1)

    def test_reflective_writing_agent(self):
        od = OntologicalDictionary()
        rwriter = ReflectiveWritingAgent("scribe", od)
        rwriter.reflect_and_write("debate", "anger", "deep thought")
        entry = rwriter.review_history()[0]
        self.assertIn("emotional_intensity", entry)
        self.assertEqual(entry["emotional_intensity"], 8)


if __name__ == "__main__":
    unittest.main()
