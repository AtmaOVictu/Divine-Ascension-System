import unittest
import random
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, dynamic_dialogue
from divine_agents.cluster import Cluster


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

    def test_dynamic_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = dynamic_dialogue(a1, a2)
        self.assertTrue(any(a.state != "Ego" for a in (a1, a2)))

    def test_cluster_synchronization(self):
        random.seed(0)
        a1 = Agent("A1")
        a2 = Agent("A2")
        cluster = Cluster([a1, a2])
        log = cluster.synchronize()
        self.assertTrue(any("transitioned" in entry for entry in log))


if __name__ == '__main__':
    unittest.main()
