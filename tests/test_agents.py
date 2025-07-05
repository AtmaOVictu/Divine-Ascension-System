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
        agent = Agent("A", state="Enotnost", language="sl")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

        agent_en = Agent("B", state="Ego", language="en")
        reply_en = agent_en.respond("What is truth?")
        self.assertIn("Truth is absolute", reply_en)

    def test_dialogue(self):
        a1 = Agent("A1", language="en")
        a2 = Agent("A2", state="Jaz", language="sl")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("Truth" in line for line in lines))

    def test_clamping(self):
        agent = Agent("Clamp", tension=5, emotion=-1)
        self.assertEqual(agent.tension, 1.0)
        self.assertEqual(agent.emotion, 0.01)

        agent.update_emotion(2)
        self.assertEqual(agent.emotion, 1.0)
        self.assertEqual(agent.tension, 1.0)

        agent.update_tension(-5)
        self.assertEqual(agent.tension, 0.01)


if __name__ == '__main__':
    unittest.main()
