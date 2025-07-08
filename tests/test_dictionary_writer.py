import unittest
from divine_agents.agent import Agent
from divine_agents.dictionary import OntologicalDictionary
from divine_agents.writer import WritingAgent
from divine_agents.dialogue import reflective_dialogue


class TestDictionaryAndWriter(unittest.TestCase):
    def test_lookup(self):
        dictionary = OntologicalDictionary()
        meaning = dictionary.get_word_meaning("anger")
        self.assertEqual(meaning["emotion"], "negative")
        self.assertGreater(meaning["emotional_intensity"], 0.5)

    def test_update(self):
        dictionary = OntologicalDictionary()
        dictionary.update_word_meaning(
            "peace",
            {
                "emotion": "positive",
                "philosophical_meaning": "state of harmony",
                "emotional_intensity": 0.1,
            },
        )
        self.assertIn("peace", dictionary.dictionary)

    def test_writing_agent(self):
        writer = WritingAgent("scribe")
        writer.write_event("test", "Ego", "reflect", 0.5)
        self.assertEqual(len(writer.transcription_history), 1)
        self.assertEqual(writer.transcription_history[0]["emotional_state"], "Ego")

    def test_reflective_dialogue(self):
        dictionary = OntologicalDictionary()
        writer = WritingAgent("scribe")
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = reflective_dialogue(a1, a2, dictionary, writer)
        self.assertTrue(any("Enotnost" in l for l in lines))
        self.assertGreaterEqual(len(writer.transcription_history), 4)


if __name__ == "__main__":
    unittest.main()
