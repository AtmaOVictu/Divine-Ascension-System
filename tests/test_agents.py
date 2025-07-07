import unittest
import os
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.pdf_utils import extract_text_from_pdf


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

    def test_pdf_extract(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'sample.pdf')
        text = extract_text_from_pdf(path)
        self.assertIn('HELLO World', text)

    def test_dialogue_with_pdf(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'sample.pdf')
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, pdf_path=path)
        self.assertTrue(any('HELLO World' in line for line in lines))


if __name__ == '__main__':
    unittest.main()
