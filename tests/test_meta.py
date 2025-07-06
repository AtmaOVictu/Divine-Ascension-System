import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestMetaHistory(unittest.TestCase):
    def test_transition_history(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz"])

    def test_decision_history(self):
        agent = Agent("B")
        agent.update_emotion(0.9)
        agent.make_moral_decision("test")
        self.assertTrue(len(agent.decisions_history) >= 1)

    def test_dialogue_history(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # verify that each agent recorded at least one moral decision
        self.assertGreaterEqual(len(a1.decisions_history), 2)
        self.assertGreaterEqual(len(a2.decisions_history), 2)
        self.assertTrue(any("Enotnost" in l for l in lines))


if __name__ == '__main__':
    unittest.main()
