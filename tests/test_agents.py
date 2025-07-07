import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.5)
        self.assertEqual(agent.transition(), "Ego")

        agent.update_emotion(0.6, "fear")
        self.assertEqual(agent.transition(), "Jaz")

    def test_response_content(self):
        agent = Agent("A", state="Enotnost", emotion_name="joy")
        agent.update_emotion(0.3)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("veseljem", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        states = [a1.state, a2.state]
        self.assertEqual(states, ["Jaz", "Enotnost"])
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
