import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.rl_agents import ReflectiveAgent, reinforced_dialogue


class TestReflectiveAgent(unittest.TestCase):
    def test_reflection_increases_tension(self):
        agent = ReflectiveAgent("A")
        initial_tension = agent.tension
        agent.reflect("fear of failure")
        self.assertGreater(agent.tension, initial_tension)

    def test_reinforced_dialogue_transitions(self):
        a1 = ReflectiveAgent("A1")
        a2 = ReflectiveAgent("A2", state="Jaz")
        convo = reinforced_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in convo))


if __name__ == "__main__":
    unittest.main()
