import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        # Trigger transition with tension
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

        # Transition from Jaz to Enotnost using emotion
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost", emotion_type="joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("joy", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Expect that agent2 eventually reaches Enotnost
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
