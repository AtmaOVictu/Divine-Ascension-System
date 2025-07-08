import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_clamping(self):
        agent = Agent("A")
        agent.update_emotion(1.5)
        self.assertLessEqual(agent.emotion, 1.0)
        self.assertLessEqual(agent.tension, 1.0)

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_question_influence(self):
        ego_agent = Agent("Ego")
        self.assertIn("absolutna", ego_agent.respond("Kaj je resnica?"))
        jaz_agent = Agent("Jaz", state="Jaz")
        self.assertIn("relativna", jaz_agent.respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, exchanges=2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertEqual(len(lines), 2 * 2 * 2)  # exchanges * agents * messages


if __name__ == '__main__':
    unittest.main()
