import unittest
from unittest.mock import patch

from divine_agents.agent import Agent
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

    @patch("divine_agents.agent.random.choice", side_effect=["happy", "happy"])
    def test_dialogue(self, mock_choice):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    @patch("divine_agents.agent.random.choice", return_value="happy")
    def test_happy_coincidence(self, mock_choice):
        a1 = Agent("A1")
        a2 = Agent("A2")
        event = a1.interact_with(a2)
        self.assertEqual(event, "happy")
        self.assertEqual(a1.state, "Jaz")


if __name__ == '__main__':
    unittest.main()
