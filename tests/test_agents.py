import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        agent2 = Agent("B")
        agent2.update_emotion(0.6)
        self.assertEqual(agent2.transition(), "Jaz")

        agent3 = Agent("C")
        agent3.update_emotion(0.4)
        agent3.update_tension(0.2)
        self.assertEqual(agent3.transition(), "Ego")

    def test_responses(self):
        agent = Agent("A", state="Enotnost", emotion_label="joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("veselje", reply)

        agent2 = Agent("B", emotion_label="fear")
        reply2 = agent2.respond("Kaj je resnica?")
        self.assertIn("strah", reply2)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # ensure emotional responses were included
        self.assertTrue(any("jeza" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
