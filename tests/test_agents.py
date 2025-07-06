import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        # Tension based transition
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        # Emotion based transition from Jaz to Enotnost
        agent.update_emotion(0.6)
        agent.transition()
        self.assertEqual(agent.state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_history_recording(self):
        agent = Agent("H")
        agent.update_tension(0.8)
        agent.transition()
        agent.update_emotion(0.6)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertGreater(len(lines), 0)


if __name__ == '__main__':
    unittest.main()
