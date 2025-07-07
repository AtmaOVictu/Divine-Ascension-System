import unittest
from divine_agents.agent import Agent
from divine_agents.cluster import Cluster
from divine_agents.dialogue import philosophical_dialogue, collective_philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A", mood="anger")
        agent.update_emotion("anger", 0.46)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("What is truth?", "en")
        self.assertIn("one", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Jaz" in line or "Enotnost" in line for line in lines))

    def test_cluster_dialogue(self):
        agents = [Agent("C1"), Agent("C2", state="Jaz")]
        cluster = Cluster(agents)
        cluster.synchronize()
        lines = collective_philosophical_dialogue(cluster)
        self.assertEqual(len(lines), 4)


if __name__ == '__main__':
    unittest.main()
