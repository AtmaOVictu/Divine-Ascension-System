import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import dynamic_dialogue
from divine_agents.system import MultiAgentLearningSystem


class TestLearningSystem(unittest.TestCase):
    def test_agent_copy(self):
        agent = Agent("A")
        agent.update_tension(0.9)
        agent.transition()
        copy = agent.copy()
        self.assertEqual(agent.history, copy.history)

    def test_dynamic_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = dynamic_dialogue(a1, a2, rounds=2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))

    def test_learning_system(self):
        agents = [Agent("A"), Agent("B")]
        system = MultiAgentLearningSystem(agents)
        system.generate_copies()
        self.assertEqual(len(system.agent_copies), 2)
        system.learn()
        self.assertTrue(all(len(a.history) > 1 for a in system.agent_copies))


if __name__ == "__main__":
    unittest.main()
