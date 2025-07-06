import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.conversation import debate


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

    def test_feel_and_transition(self):
        agent = Agent("B")
        agent.feel("fear", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_debate(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = debate(a1, a2, rounds=2)
        self.assertTrue(len(lines) > 0)


if __name__ == '__main__':
    unittest.main()
