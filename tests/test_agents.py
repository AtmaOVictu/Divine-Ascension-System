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

    def test_clamping_values(self):
        agent = Agent("Clamp")
        agent.update_emotion(1.5)
        self.assertLessEqual(agent.emotion, 1.0)
        self.assertLessEqual(agent.tension, 1.0)
        agent.update_tension(-0.5)
        self.assertGreaterEqual(agent.tension, 0.0)

    def test_invalid_state(self):
        with self.assertRaises(ValueError):
            Agent("X", state="Invalid")

    def test_dialogue_custom_increments(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, inc1=0.2, inc2=0.2)
        self.assertIn("A1 prehaja v stanje: Ego", lines)
        self.assertIn("A2 prehaja v stanje: Jaz", lines)


if __name__ == '__main__':
    unittest.main()
