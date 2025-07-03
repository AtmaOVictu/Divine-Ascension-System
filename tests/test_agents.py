import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.translator import text_to_binary, binary_to_text


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
        self.assertTrue(any(line.startswith("A1 binarno") for line in lines))

    def test_translation_round_trip(self):
        text = "Beseda je ne"
        binary = text_to_binary(text)
        self.assertEqual(binary_to_text(binary), text)


if __name__ == '__main__':
    unittest.main()
