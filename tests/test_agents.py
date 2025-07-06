import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents import Agent, AgentGroup, philosophical_dialogue, group_dialogue


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

    def test_group_attribute(self):
        agent = Agent("G", group=AgentGroup.DUALISTIC)
        self.assertEqual(agent.group, AgentGroup.DUALISTIC)

    def test_group_dialogue(self):
        agents = [
            Agent("A1", group=AgentGroup.DUALISTIC),
            Agent("A2", state="Jaz", group=AgentGroup.RELATIONAL),
        ]
        lines = group_dialogue(agents)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
