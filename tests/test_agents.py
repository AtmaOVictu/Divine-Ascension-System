import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from divine_agents import Agent, philosophical_dialogue, Environment


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply.lower())

    def test_dialogue(self):
        env = Environment()
        env.update_condition("social_pressure", 0.8)
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, env)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_environment_influence(self):
        env = Environment()
        env.update_condition("social_pressure", 0.8)
        agent = Agent("X")
        env.influence_agent(agent)
        self.assertGreater(agent.emotion, 0)


if __name__ == '__main__':
    unittest.main()
