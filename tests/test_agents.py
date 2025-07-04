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

    def test_dialogue_default(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dialogue_low_emotion(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, agent1_emotion=0.3, agent2_emotion=0.3)
        # emotions below threshold should keep states unchanged
        self.assertFalse(any("Jaz" in line for line in lines if "prehaja" in line and "A1" in line))
        self.assertFalse(any("Enotnost" in line for line in lines if "prehaja" in line and "A2" in line))

    def test_dialogue_custom_emotion(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, agent1_emotion=0.9, agent2_emotion=0.9)
        self.assertTrue(any("Jaz" in line for line in lines if "prehaja" in line and "A1" in line))
        self.assertTrue(any("Enotnost" in line for line in lines if "prehaja" in line and "A2" in line))


if __name__ == '__main__':
    unittest.main()
