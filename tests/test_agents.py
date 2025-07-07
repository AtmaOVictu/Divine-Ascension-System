import unittest

from divine_agents.agent import Agent
from divine_agents.cluster import Cluster
from divine_agents.dialogue import philosophical_dialogue, collective_philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_dynamic_threshold_with_anger(self):
        agent = Agent("A")
        agent.update_emotion("anger", 0.51)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost", language="sl")
        reply_sl = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply_sl)
        reply_en = agent.respond("What is truth?", language="en")
        self.assertIn("one", reply_en)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("transitions" in line for line in lines))

    def test_cluster_dialogue(self):
        c = Cluster([Agent("A1"), Agent("A2", state="Jaz")])
        lines = collective_philosophical_dialogue(c)
        self.assertEqual(len(lines), 2)


if __name__ == '__main__':
    unittest.main()
