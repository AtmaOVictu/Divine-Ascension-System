import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.cluster import Cluster


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A", mood="anger")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost", mood="joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1", mood="anger")
        a2 = Agent("A2", state="Jaz", mood="joy")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_cluster(self):
        a1 = Agent("C1", mood="anger", emotion=0.9)
        a2 = Agent("C2", mood="joy", emotion=0.9)
        cluster = Cluster([a1, a2])
        cluster.synchronize()
        dialogue = cluster.display_dialogue()
        self.assertEqual(len(dialogue), 2)


if __name__ == '__main__':
    unittest.main()
