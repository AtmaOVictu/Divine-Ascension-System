import unittest
from divine_agents.agent import Agent
import random
from divine_agents.dialogue import philosophical_dialogue, philosophical_debate
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


class TestCluster(unittest.TestCase):
    def test_synchronize(self):
        rng = random.Random(0)
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        a3 = Agent("A3")
        cluster = Cluster([a1, a2, a3])
        cluster.synchronize(rng=rng)
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Jaz")
        self.assertEqual(a3.state, "Jaz")

    def test_debate(self):
        a1 = Agent("A1", tension=0.4, emotion=0.4)
        a2 = Agent("A2", state="Jaz", tension=0.4, emotion=0.4)
        lines = philosophical_debate(a1, a2)
        self.assertEqual(a1.state, "Jaz")
        self.assertTrue(any("Resnica" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
