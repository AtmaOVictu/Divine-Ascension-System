import unittest
import random
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.cluster import Cluster


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A", rationality=0.9)
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_blocked_by_rationality(self):
        agent = Agent("A", rationality=0.4)
        agent.update_emotion(0.9)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        random.seed(5)
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_cluster_sync(self):
        random.seed(0)
        agents = [Agent("A1"), Agent("A2", state="Jaz")]
        cluster = Cluster(agents)
        reflections = cluster.synchronize()
        self.assertEqual(len(reflections), 2)
        self.assertIn("I am", reflections[0])


if __name__ == '__main__':
    unittest.main()
