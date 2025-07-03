import unittest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from divine_agents.agent import Agent, NegationAgent
from divine_agents.dialogue import philosophical_dialogue, philosophical_debate


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


class TestNegationAgent(unittest.TestCase):
    def test_negation_action(self):
        agent = NegationAgent("N", negation_factor=2)
        action = agent.perform_action("ustvari")
        self.assertEqual(action, "\u00ac(\u00ac(ustvari))")
        self.assertIn(action, agent.history)

    def test_debate(self):
        a1 = NegationAgent("A1")
        a2 = NegationAgent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2)
        self.assertTrue(any("Enotnost" in l for l in lines))


if __name__ == '__main__':
    unittest.main()
