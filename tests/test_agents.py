import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent, Emotions, State
from divine_agents.debate import Debate


class AgentSystemTest(unittest.TestCase):
    def test_transition_ego_to_jaz(self):
        agent = Agent("A", state=State.EGO, tension=0.8)
        agent.update_state()
        self.assertEqual(agent.state, State.JAZ)

    def test_transition_jaz_to_enotnost(self):
        agent = Agent("B", state=State.JAZ, tension=0.8)
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
        debate = Debate(a, b)
        resp_a, resp_b = debate.step()
        self.assertIn("absolute", resp_a)
        self.assertIn("relative", resp_b)


if __name__ == "__main__":
    unittest.main()
