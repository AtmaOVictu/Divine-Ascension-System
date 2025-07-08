import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import (
    philosophical_dialogue,
    philosophical_dialogue_with_writer,
)
from divine_agents.dictionary import OntologicalDictionary
from divine_agents.writer import WritingAgent


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


class TestDictionaryAndWriter(unittest.TestCase):
    def test_dictionary_lookup(self):
        dictionary = OntologicalDictionary()
        meaning = dictionary.get_word_meaning("fear")
        self.assertEqual(meaning["emotion"], "negative")

    def test_writer_records(self):
        writer = WritingAgent("scribe")
        writer.write_event("start", "Ego", "init")
        self.assertEqual(len(writer.review_history()), 1)

    def test_dialogue_with_writer(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        dictionary = OntologicalDictionary()
        writer = WritingAgent("scribe")
        lines = philosophical_dialogue_with_writer(a1, a2, writer, dictionary)
        self.assertTrue(len(writer.review_history()) >= 3)
        self.assertIn(a1.state, {"Jaz", "Enotnost"})
        self.assertTrue(any("resnica" in line.lower() for line in lines))


if __name__ == "__main__":
    unittest.main()
