import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.multi_layer import MultiLayeredAgent
from divine_agents.dynamics import EmotionalTensionDynamics


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

    def test_multi_layer(self):
        agent = Agent("B", state="Jaz", loyalty=0.9, experiences=["selfish act"])
        wrapper = MultiLayeredAgent(agent)
        wrapper.multi_layer_transition()
        self.assertEqual(agent.state, "Enotnost")

    def test_emotional_dynamics(self):
        agent = Agent("C", tension=0.3)
        agent.emotion = 'fear'
        dyn = EmotionalTensionDynamics(agent)
        dyn.adjust_tension()
        self.assertGreater(agent.tension, 0.3)


if __name__ == '__main__':
    unittest.main()
