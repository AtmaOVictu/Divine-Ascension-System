import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.ontology import OntologicalDictionary
from divine_agents.writing import WritingAgent


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

    def test_dictionary_lookup(self):
        dictionary = OntologicalDictionary()
        meaning = dictionary.get_word_meaning("truth")
        self.assertEqual(meaning["philosophical_meaning"], "the essence of reality")

    def test_writing_agent_logs(self):
        writer = WritingAgent("Tester")
        writer.write_event("test", "calm", "reflection")
        self.assertEqual(len(writer.review_history()), 1)


if __name__ == '__main__':
    unittest.main()
