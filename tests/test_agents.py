import unittest
import random
from divine_agents import Agent, philosophical_dialogue, Cluster


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        agent.update_rationality(0.9)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("Čutim", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_cluster(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        cluster = Cluster([a1, a2])
        random.seed(0)
        lines = cluster.synchronize()
        self.assertEqual(len(lines), 2)


if __name__ == '__main__':
    unittest.main()
