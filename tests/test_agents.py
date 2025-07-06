import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_trigger(self):
        agent = Agent("B")
        agent.update_emotion(0.6, "fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertIn("[fear]", agent.respond("Kaj je resnica?"))

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # A1 should transition to Jaz and A2 to Enotnost
        self.assertTrue(any("Jaz" in line for line in lines if "A1" in line))
        self.assertTrue(any("Enotnost" in line for line in lines if "A2" in line))


if __name__ == '__main__':
    unittest.main()
