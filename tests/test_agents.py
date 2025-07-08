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
        agent.update_tension(1.5)
        self.assertEqual(agent.tension, 1.0)
        agent.update_tension(-1)
        self.assertEqual(agent.tension, 0.0)
        agent.update_emotion(1.2)
        self.assertEqual(agent.emotion, 1.0)
        self.assertEqual(agent.tension, 1.0)

    def test_transition_after_clamping(self):
        agent = Agent("A")
        agent.update_tension(1.2)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        agent = Agent("B")
        agent.update_emotion(1.3)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_boundary(self):
        a1 = Agent("A")
        a1.update_tension(0.7)
        self.assertEqual(a1.transition(), "Ego")

        a2 = Agent("B")
        a2.update_emotion(0.5)
        self.assertEqual(a2.transition(), "Ego")

        a3 = Agent("C")
        a3.update_tension(0.71)
        self.assertEqual(a3.transition(), "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
