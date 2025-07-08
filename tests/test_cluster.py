import unittest
from divine_agents import Agent, AgentCluster, PhilosophicalDialogue


class TestAgentCluster(unittest.TestCase):
    def test_cluster_unified(self):
        cluster = AgentCluster()
        a1 = Agent("A1")
        a2 = Agent("A2")
        a1.update_emotion(0.8)
        a2.update_emotion(0.8)
        cluster.add_agent(a1)
        cluster.add_agent(a2)
        cluster.transition_agents()
        cluster.transition_agents()
        cluster.update_cluster_state()
        self.assertEqual(cluster.cluster_state, "Unified")

    def test_dialogue_class(self):
        a1 = Agent("X")
        a2 = Agent("Y", state="Jaz")
        dialogue = PhilosophicalDialogue(a1, a2)
        lines = dialogue.exchange_dialogue()
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
