import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from divine_agents.agent import Agent, State
from divine_agents.dialogue import philosophical_dialogue, dialogue_step


class AgentSystemTest(unittest.TestCase):
    def test_transition_ego_to_jaz(self):
        agent = Agent("A")
        agent.tension = 0.8
        agent.update_state()
        self.assertEqual(agent.state, State.JAZ)

    def test_transition_jaz_to_enotnost(self):
        agent = Agent("B", state=State.JAZ, tension=0.9)
        agent.update_state()
        self.assertEqual(agent.state, State.ENOTNOST)

    def test_emotion_triggered_transition(self):
        agent = Agent("C")
        agent.feel(fear=0.6)
        agent.update_state()
        self.assertEqual(agent.state, State.JAZ)

    def test_dialogue_responses(self):
        a = Agent("A", state=State.EGO)
        b = Agent("B", state=State.JAZ)
        lines = philosophical_dialogue(a, b)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dialogue_step(self):
        a = Agent("A")
        b = Agent("B")
        resp_a, resp_b = dialogue_step(a, b)
        self.assertIn("Resnica", resp_a)
        self.assertIn("Resnica", resp_b)


if __name__ == "__main__":
    unittest.main()
