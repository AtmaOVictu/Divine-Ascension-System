import unittest
from divine_agents.agent import Agent
from unittest.mock import patch
from divine_agents.dialogue import philosophical_dialogue


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

    def test_dialogue_parameters(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, emotion_inc1=0.8, emotion_inc2=0.6)
        self.assertIn("Jaz", lines[2])
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dialogue_random(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        with patch('divine_agents.dialogue.random.uniform', side_effect=[0.8, 0.6, 0.1, 0.1]):
            lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
