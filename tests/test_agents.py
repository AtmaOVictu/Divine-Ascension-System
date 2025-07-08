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
        lines = philosophical_dialogue(a1, a2, emotion_increase=0.6, exchanges=2)
        self.assertEqual(len(lines), 4)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_clamping(self):
        agent = Agent("A")
        agent.update_emotion(1.5)
        self.assertLessEqual(agent.emotion, 1.0)
        self.assertLessEqual(agent.tension, 1.0)
        agent.update_tension(-0.5)
        self.assertGreaterEqual(agent.tension, 0.0)

    def test_history_accumulation(self):
        agent = Agent("A")
        philosophical_dialogue(agent, Agent("B"), exchanges=3)
        # initial state plus three transitions
        self.assertEqual(len(agent.history), 4)

    def test_question_context(self):
        agent = Agent("A")
        response = agent.respond("Kako si?")
        self.assertIn("Nimam odgovora", response)


if __name__ == '__main__':
    unittest.main()
