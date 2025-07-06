import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A")
        self.assertIn("absolutna", agent.respond("Kaj je resnica?"))
        agent.state = "Jaz"
        self.assertIn("relativna", agent.respond("Kaj je resnica?"))
        agent.state = "Enotnost"
        self.assertIn("eno", agent.respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, rounds=1)
        joined = " ".join(lines)
        self.assertIn("Jaz", joined)
        self.assertTrue(any(word in joined for word in ["Enotnost", "Jaz"]))


if __name__ == '__main__':
    unittest.main()
