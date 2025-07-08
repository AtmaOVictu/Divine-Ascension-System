import unittest
from divine_agents.agent import Agent
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

    def test_fame_boxes(self):
        agent = Agent("F")
        agent.update_fame(positive_actions=100, negative_actions=0, participation_score=50)
        self.assertEqual(agent.boxes["fame"], "Legendary Fame Box")

    def test_cluster(self):
        agent = Agent("C")
        agent.fame = 0.6
        agent.boxes["fame"] = agent.get_fame_box()
        agent.clusters["social_cluster"] = [agent.boxes["fame"], agent.boxes["emotional_state"]]
        self.assertIn("Influential Fame Box", agent.get_cluster_boxes("social_cluster"))


if __name__ == '__main__':
    unittest.main()
