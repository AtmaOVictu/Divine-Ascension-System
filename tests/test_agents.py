import unittest
from unittest.mock import patch

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.codex import Codex


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.8)
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("Z veseljem"))
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_codex_interaction(self):
        a1 = Agent("AA1")
        a2 = Agent("AA2")
        codex = Codex()
        codex.add_element(a1)
        codex.add_element(a2)
        with patch("random.uniform", return_value=0.8):
            codex.simulate_interaction(a1, a2)
        self.assertIn(a1.state, ("Jaz", "Enotnost"))
        self.assertIn(a2.state, ("Jaz", "Enotnost"))


if __name__ == '__main__':
    unittest.main()
