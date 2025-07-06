import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from divine_agents.agent import Agent, State
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, State.JAZ)

    def test_responses(self):
        agent = Agent("A", state=State.ENOTNOST)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state=State.JAZ)
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_emotional_response(self):
        agent = Agent("B")
        agent.update_emotion(0.9)
        agent.transition()
        self.assertIn("močno", agent.respond("Kaj je resnica?"))


if __name__ == '__main__':
    unittest.main()
