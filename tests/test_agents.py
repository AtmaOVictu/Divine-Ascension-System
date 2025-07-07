import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


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

    def test_reward_and_xp(self):
        agent = Agent("A")
        agent.reward(True)
        self.assertEqual(agent.xp, 10)
        agent.reward(False)
        self.assertEqual(agent.xp, 5)

    def test_level_up(self):
        agent = Agent("A", xp=100)
        agent.level_up()
        self.assertEqual(agent.state, "Nov nivo")
        self.assertEqual(agent.xp, 0)


if __name__ == '__main__':
    unittest.main()
