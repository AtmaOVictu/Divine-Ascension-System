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

    def test_emotion_clamping(self):
        agent = Agent("A")
        agent.update_emotion(1.5)
        self.assertLessEqual(agent.emotion, 1.0)
        self.assertLessEqual(agent.tension, 1.0)

    def test_history_accumulation(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        agent.transition()
        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, exchanges=2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_parameterized_dialogue(self):
        a1 = Agent("X")
        a2 = Agent("Y")
        philosophical_dialogue(a1, a2, emotion1=0.9, emotion2=0.9, exchanges=1)
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Jaz")


if __name__ == '__main__':
    unittest.main()
