import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.ontology import OntologicalDictionary
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
        self.assertTrue(any(state in line for state in ["Jaz", "Enotnost"] for line in lines))

    def test_dictionary_lookup(self):
        ontology = OntologicalDictionary()
        meaning = ontology.get_word_meaning("anger")
        self.assertEqual(meaning["emotion"], "negative")

    def test_writer_records_event(self):
        writer = WritingAgent("A")
        writer.write_event("Test", "happy", "reflection")
        self.assertEqual(len(writer.review_history()), 1)

    def test_emotional_response(self):
        agent = Agent("A")
        agent.update_emotion(0.9)
        response = agent.respond("Kaj je resnica?")
        self.assertIn("Čutim", response)


if __name__ == '__main__':
    unittest.main()
