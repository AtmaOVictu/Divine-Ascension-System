import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.environment import Environment


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

    def test_environment_influence(self):
        env = Environment("H", "harmonious")
        agent = Agent("B")
        env.influence(agent)
        self.assertEqual(agent.state, "Jaz")

    def test_disharmony_transition(self):
        env = Environment("D", "disharmonious")
        agent = Agent("C", state="Jaz")
        env.influence(agent)
        self.assertEqual(agent.state, "Enotnost")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        env1 = Environment("E1", "harmonious")
        env2 = Environment("E2", "disharmonious")
        lines = philosophical_dialogue(a1, a2, env1, env2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
