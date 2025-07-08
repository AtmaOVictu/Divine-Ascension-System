import unittest
from divine_agents.agent import Agent
from divine_agents.cluster import AgentCluster
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
        self.assertTrue(any("\u010custvo" in line for line in lines))


class TestAgentCluster(unittest.TestCase):
    def test_cluster_unified(self):
        cluster = AgentCluster()
        a1 = Agent("C1")
        a2 = Agent("C2", state="Jaz")
        cluster.add_agent(a1)
        cluster.add_agent(a2)
        a1.update_tension(0.8)
        a2.update_tension(0.8)
        cluster.transition_agents()
        cluster.transition_agents()
        cluster.update_cluster_state()
        self.assertEqual(cluster.cluster_state, "Unified")

    def test_synchronize_emotions(self):
        cluster = AgentCluster()
        a1 = Agent("C1", emotion=0.0)
        a2 = Agent("C2", emotion=1.0)
        cluster.add_agent(a1)
        cluster.add_agent(a2)
        cluster.synchronize_emotions()
        self.assertAlmostEqual(a1.emotion, 0.5)
        self.assertAlmostEqual(a2.emotion, 0.5)


if __name__ == '__main__':
    unittest.main()
